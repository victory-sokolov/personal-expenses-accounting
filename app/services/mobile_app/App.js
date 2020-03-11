import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import React from 'react';
import {StyleSheet, View} from 'react-native';
import CameraActivity from './components/CameraActivity';
import HomeScreen from './components/HomeScreen';

import {createStackNavigator} from 'react-navigation-stack';
import {createAppContainer} from 'react-navigation';
import Home from './components/HomeScreen';
import CameraActivity from './components/CameraActivity';

const Navigator = createStackNavigator({
  Home: {screen: Home},
  Camera: {screen: CameraActivity},
});

const App = createAppContainer(Navigator);

export default App;
