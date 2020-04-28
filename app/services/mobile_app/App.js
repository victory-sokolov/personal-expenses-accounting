import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import CameraActivity from './components/CameraActivity';
import Home from './components/HomeScreen';
import Login from './components/Login';


const Navigator = createStackNavigator({
  Login: {screen: Login},
  Home: {screen: Home},
  Camera: {screen: CameraActivity}

});

const App = createAppContainer(Navigator);

export default App;
