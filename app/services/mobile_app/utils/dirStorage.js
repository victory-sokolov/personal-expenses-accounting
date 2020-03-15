import { Platform } from 'react-native';
const RNFS = require('react-native-fs');

export const dirHome = Platform.select({
  ios: `${RNFS.DocumentDirectoryPath}/ReceiptApp`,
  android: `${RNFS.ExternalDirectoryPath}/ReceiptApp`,
});

export const dirPictures = `${dirHome}/Pictures`;
