import React, { Component } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { HOST_IP } from 'react-native-dotenv';
import { Button, Input } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';
export default class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      password: '',
    };
  }


  formUpload = () => {
      const {navigate} = this.props.navigation;
      fetch(`http://${HOST_IP}:5000/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: this.state.email,
          password: this.state.password,
        }),
      })
        .then(response =>
          response
            .json()
            .then(data => ({status: response.status, body: data}))
            .then(res => {
              if (res.status == 200) {
                navigate('Home', {
                  id: res.body.id,
                });
              }
            }),
        )
        .catch(error => {
          console.log(`Error: ${error}`);
        });

  };

  render() {
    return (
      <View style={styles.container}>
        <View>
          <Text style={styles.heading}>
            Welcome
          </Text>
          <Input
            name="email"
            placeholder="Email"
            required="required"
            value={this.state.email}
            errorStyle={{color: 'red'}}
            onChangeText={text =>
              this.setState({email: text})
            }
            leftIcon={
              <Icon
                name="envelope-o"
                size={24}
                color="black"
              />
            }
          />
          <Input
            name="password"
            placeholder="Password"
            required="required"
            secureTextEntry={true}
            errorStyle={{color: 'red'}}
            leftIcon={
              <Icon
                name="lock"
                size={24}
                color="black"
              />
            }
            onChangeText={text =>
              this.setState({password: text})
            }
          />
          <Button
            color="blue"
            title="Log In"
            containerStyle={{marginTop: 25}}
            onPress={this.formUpload}
          />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    marginTop: 130,
  },
  heading: {
    textAlign: 'center',
    fontSize: 28,
    fontWeight: 'bold',
    paddingBottom: 25,
  }
});