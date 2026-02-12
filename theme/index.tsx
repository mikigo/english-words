import {
  Layout as BasicLayout,
  getCustomMDXComponent as basicGetCustomMDXComponent,
} from '@rspress/core/theme-original';
import './index.css';

const myStyle = {
  fontSize: '2em',
  fontWeight: 'bold',
  center: true,
}

const Layout = () => (
  <BasicLayout
    beforeFeatures={
          <div>
            <h1 align="center"  style={myStyle}>
              分类列表
            </h1>
          </div>
        }
  />
);

export { Layout };
export * from '@rspress/core/theme-original';