<p align="center"><img src="https://www.tchap.gouv.fr/themes/tchap/img/logos/tchap-logo.svg" width="300" alt="tchap-logo" /></p>

# Tchap compound Web

[![](https://img.shields.io/badge/-Storybook-ff4785?logo=Storybook&logoColor=white&style=flat-square)](https://tchapgouv.github.io/compound-web/) [![](https://img.shields.io/github/license/tchapgouv/compound)](https://github.com/tchapgouv/compound/blob/main/LICENSE)

React implementation of Compound – Tchap's design system based on Element– See full documentation on https://tchapgouv.github.io/compound-web/

It is a soft fork of the element compound-web, but using Tchap `compound-design-token` https://github.com/tchapgouv/compound-design-tokens `main` branch

## New release

When a new version of `compound-design-token` is avalaible, the `yarn.lock` of this package also needs to be updated.

```
rm -rf yarn.lock
yarn install
```

## Development

| Command                    | Runs                          |
| -------------------------- | ----------------------------- |
| `yarn dev`                 | Runs a local Storybook server |
| `yarn lint`                | Lints all components          |
| `yarn gen:component $name` | Bootstraps a new component    |

### Testing

| Command              | Runs                              |
| -------------------- | --------------------------------- |
| `yarn test`          | Runs unit tests                   |
| `yarn e2e:docker`    | Runs end-to-end tests             |
| `yarn e2e:docker -u` | Updates end-to-end test snapshots |

All components are expected to come with comprehensive unit tests and visual tests. We use Playwright to run visual tests on every story present in Storybook, so story coverage is really important! It helps us validate component implementations against the designs and prevents visual regressions at the same time.

We recommend running the end-to-end tests via Docker as shown above to get consistent text rendering for screenshots.

### Linking

If you want to work on Compound Web as a linked package within a larger React application, TypeScript might complain about there being multiple copies of @types/react in the tree. You can work around this by linking Compound Web's copy of @types/react to your application's copy:

```bash
$ cd my-application/node_modules/@types/react
$ yarn link
$ cd ../../../../compound-web
$ yarn link @types/react
```

## Copyright & License

Copyright (c) 2023-2025 New Vector Ltd
2025, Direction interministérielle du numérique

This software is multi licensed by New Vector Ltd (Element). It can be used either:

(1) for free under the terms of the GNU Affero General Public License (as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version); OR

(2) under the terms of a paid-for Element Commercial License agreement between you and Element (the terms of which may vary depending on what you and Element have agreed to).
Unless required by applicable law or agreed to in writing, software distributed under the Licenses is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the Licenses for the specific language governing permissions and limitations under the Licenses.
