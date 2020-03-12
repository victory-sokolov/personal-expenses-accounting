import CameraActivity from './components/CameraActivity';
import Home from './components/HomeScreen';

import {createStackNavigator} from 'react-navigation-stack';
import {createAppContainer} from 'react-navigation';

const Navigator = createStackNavigator({
  Home: {screen: Home},
  Camera: {screen: CameraActivity},
});

const App = createAppContainer(Navigator);

export default App;
