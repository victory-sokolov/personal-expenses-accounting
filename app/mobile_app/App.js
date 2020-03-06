import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { RNCamera } from 'react-native-camera';

const App = () => {
  return (
    <View>
      <RNCamera style={styles.cameraStyles} />
      <Text>Take Photo</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  cameraStyles: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
  },
});

export default App;
