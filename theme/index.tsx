import './index.css';

import Theme from 'rspress/theme';

const myStyle = {
  fontSize: '2em',
  fontWeight: 'bold',
  center: true,
}

const Layout = () => (
    <Theme.Layout
        afterHero={
          <div>
            <h1 align="center"  style={myStyle}>
              我创建的开源项目
            </h1>
          </div>
        }
    />
);

export default {
  ...Theme,
  Layout,
};

export * from 'rspress/theme';