import React from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import Icon from 'react-native-vector-icons/EvilIcons';
class HomeScreen extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      id: this.props.navigation.state.params.id
    }
  }

  render() {
    const {navigate} = this.props.navigation;
    return (
      <View style={styles.container}>
        <View style={styles.content}>
          <Text>
          </Text>
        </View>
        <View style={styles.footer}>
          <TouchableOpacity
            style={styles.cameraButton}
            onPress={() => navigate('Camera', {id:this.state.id})}>
            <Icon name="camera" size={35} color="#fff" />
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}

;

const styles = StyleSheet.create({
  container : {
    flex: 1,
  },
  cameraButton: {
    shadowColor: 'black',
    shadowOpacity: 0.9,
    elevation: 12,
    borderColor: 'rgba(0,0,0,0.2)',
    alignItems: 'center',
    justifyContent: 'center',
    width: 70,
    height: 70,
    backgroundColor: '#1E90FF',
    borderRadius: 50,
  },
  content: {
    flex: 1,
  },
  footer: {
    height: 100,
    alignItems: 'center',
    paddingBottom: 25,
  },
});

export default HomeScreen;
