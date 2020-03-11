import React from 'react';
import {Dimensions, StyleSheet, View} from 'react-native';
import {Camera} from 'react-native-camera';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

class CameraActivity extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Camera
          ref={cam => {
            this.camera = cam;
          }}
          style={styles.preview}
          aspect={Camera.constants.Aspect.fill}
        />
        <Icon
          name="camera-iris"
          size={45}
          color="#fff"
          onPress={this.takePicture.bind(this)}
        />
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
});

export default CameraActivity;
