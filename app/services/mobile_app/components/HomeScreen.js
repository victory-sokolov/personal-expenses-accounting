import React from 'react';
import {View, Text, Button, StyleSheet, TouchableOpacity} from 'react-native';
import Icon from 'react-native-vector-icons/EvilIcons';

import CameraIcon from 'react-native-vector-icons/MaterialCommunityIcons';



class HomeScreen extends React.Component {

  render() {

    const { navigate } = this.props.navigation;
    return (
      <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
        <View style={styles.footer}>
          <TouchableOpacity
              style={styles.cameraButton} 
              onPress = {() => navigate(
              'Camera'
            )} >
            <Icon name="camera" size={32} color='#fff'/>
          </TouchableOpacity>       
        </View>

      </View>
    )
  }
}

const styles = StyleSheet.create({

  cameraButton: {
    borderWidth:1,
    borderColor:'rgba(0,0,0,0.2)',
    alignItems:'center',
    justifyContent:'center',
    width:50,
    height:50,
    backgroundColor:'#1E90FF',
    borderRadius:50,
  },
  footer: {
    flex: 1,
    justifyContent:'flex-end',
    paddingBottom: 25,
  }
});

export default HomeScreen;
