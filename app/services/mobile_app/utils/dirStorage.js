import { Platform } from 'react-native';
const RNFS = require('react-native-fs');

export const dirHome = Platform.select({
  ios: RNFS.DocumentDirectoryPath,
  android: RNFS.DocumentDirectoryPath,
});

export const dirPictures = `${dirHome}/Pictures`;
