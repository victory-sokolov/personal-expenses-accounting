import React from 'react';
import { Dimensions, StyleSheet, TouchableOpacity, View } from 'react-native';
import { RNCamera } from 'react-native-camera';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
import { withNavigationFocus } from 'react-navigation';
import { dirPictures } from '../utils/dirStorage';
const RNFS = require('react-native-fs');

class CameraActivity extends React.Component {
  render() {
    const {isFocused} = this.props;
    return (
      <View style={styles.container}>
        {isFocused && (
          <RNCamera
            ref={cam => {
              this.camera = cam;
            }}
            flashMode={RNCamera.Constants.FlashMode.auto}
            playSoundOnCapture={true}
            style={styles.preview}>
            <TouchableOpacity
              onPress={this.takePicture.bind(this)}
              style={styles.capture}>
              <Icon name="camera-iris" size={80} style={styles.cameraIcon} />
            </TouchableOpacity>
          </RNCamera>
        )}
      </View>
    );
  }

  takePicture = async () => {
    if (this.camera) {
      const options = {
        quality: 0.5,
        base64: true,
        fixOrientation: true,
      };
      const data = await this.camera.takePictureAsync(options);
      this.saveImage(data.uri);
      console.log(data.uri);
    }
  };

  //move the attachment to app folder
  moveAttachment = async (filePath, newFilepath) => {
    console.log(`DIR: ${dirPictures}`);
    return new Promise((resolve, reject) => {
      RNFS.mkdir(dirPictures)
        .then(() => {
          RNFS.moveFile(filePath, newFilepath)
            .then(() => {
              console.log('FILE MOVED', filePath, newFilepath);
              resolve(true);
            })
            .catch(error => {
              console.log('moveFile error', error);
              reject(error);
            });
        })
        .catch(err => {
          console.log('mkdir error', err);
          reject(err);
        });
    });
  };

  saveImage = async filePath => {
    try {
      const newImageName = 'output.jpg';
      const newFilepath = `${dirPictures}/${newImageName}`;
      // move and save image to new filepath
      const imageMoved = await this.moveAttachment(filePath, newFilepath);
      console.log('image moved', imageMoved);
    } catch (error) {
      console.log(error);
    }
  };
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  preview: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
    height: Dimensions.get('window').height,
    width: Dimensions.get('window').width,
  },
  cameraIcon: {
    color: '#fff',
    paddingBottom: 30,
  },
});

export default withNavigationFocus(CameraActivity);
