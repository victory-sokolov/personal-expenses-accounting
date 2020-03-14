import React from 'react';
import { StyleSheet, TouchableOpacity, View } from 'react-native';
import Icon from 'react-native-vector-icons/EvilIcons';


class HomeScreen extends React.Component {

  render() {
    const { navigate } = this.props.navigation;
    return (
      <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
        <View style={styles.footer}>
          <TouchableOpacity
            style={styles.cameraButton}
            onPress={() => navigate('Camera')}>
            <Icon name="camera" size={35} color="#fff" />
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({

  cameraButton: {
    shadowColor: 'black',
    shadowOpacity: 0.9,
    elevation: 12,
    borderColor:'rgba(0,0,0,0.2)',
    alignItems:'center',
    justifyContent:'center',
    width:60,
    height:60,
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
