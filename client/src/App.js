import {
  Button,
  CssBaseline,
  ThemeProvider,
  createMuiTheme,
  makeStyles,
} from '@material-ui/core';
import {
  ActionRequest,
  AudioActionResponse,
  ChatController,
  FileActionResponse,
  MuiChat,
} from 'chat-ui-react';
import React from 'react';

const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#007aff',
    },
  },
});

const useStyles = makeStyles(() => ({
  root: {
    backgroundColor: 'gray',
  },
  container: {
    minHeight: '100vh',
    height: '100vh',
    maxWidth: '640px',
    marginLeft: 'auto',
    marginRight: 'auto',
  },
}));

export default function App() {
  const classes = useStyles();
  const [chatCtl] = React.useState(new ChatController());

  React.useMemo(async () => {
    await chatCtl.addMessage({
      type: 'text',
      content: `Please enter something.`,
      self: false,
    });
    chatCtl.setActionRequest({ type: 'text', always: true }, (res) =>
      chatCtl.addMessage({
        type: 'text',
        content: `You have entered:\n${res.value}`,
        self: false,
      }),
    );
  }, [chatCtl]);

  return (
    <div className={classes.root}>
      <div className={classes.container}>
        <MuiChat chatController={chatCtl} />
      </div>
    </div>
  );
}