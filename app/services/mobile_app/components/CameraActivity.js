import React from 'react';
import { Dimensions, StyleSheet, TouchableOpacity, View } from 'react-native';
import { RNCamera } from 'react-native-camera';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

class CameraActivity extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <RNCamera
          ref={cam => {
            this.camera = cam;
          }}
          style={styles.preview}>
          <TouchableOpacity
            onPress={() => this.takePicture(this.camera)}
            style={styles.capture}
          >
          <Icon name="camera-iris" size={60} style={styles.cameraIcon} />
          </TouchableOpacity>
        </RNCamera>
      </View>
    );
  }

  takePicture() {
    this.camera
      .capture()
      .then(data => console.log(data))
      .catch(err => console.error(err));
  }
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
    color: "#fff",
    paddingBottom: 20,
  },
});

export default CameraActivity;
