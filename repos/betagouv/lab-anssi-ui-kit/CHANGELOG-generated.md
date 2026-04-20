## Changelog : lab-anssi-ui-kit (30 derniers jours, au 16 avril 2026)

### Résumé
Cette version apporte des améliorations significatives aux composants existants, notamment les onglets (Tabs), les en-têtes (Header) et les liens (Link), avec l'ajout de nouvelles fonctionnalités comme la gestion de slots personnalisés et des options de configuration plus fines. Des correctifs de sécurité ont également été appliqués et les dépendances ont été mises à jour pour assurer la stabilité et la performance de la bibliothèque.

### Évolutions fonctionnelles
- Ajout du composant Tabs et Tabnav, permettant la création d'interfaces avec des onglets. [#83edacb](https://github.com/betagouv/lab-anssi-ui-kit/commit/83edacb)
- Amélioration du composant DsfrHeader avec l'ajout de slots pour personnaliser la barre de navigation et les liens d'outils, offrant une plus grande flexibilité. [#6958024](https://github.com/betagouv/lab-anssi-ui-kit/commit/6958024)
- Ajout de la gestion des ToolLinks via une prop dédiée dans le composant DsfrHeader. [#b0e720a](https://github.com/betagouv/lab-anssi-ui-kit/commit/b0e720a)
- Ajout d'une story d'exemple dédiée au Header MSS dans le composant DsfrHeader. [#e20f5b0](https://github.com/betagouv/lab-anssi-ui-kit/commit/e20f5b0)
- Ajout d'un slot 'hint' au composant DsfrCheckbox pour permettre l'ajout d'informations complémentaires. [#633d112](https://github.com/betagouv/lab-anssi-ui-kit/commit/633d112)
- Ajout d'un slot 'description' au composant DsfrFooter pour une description plus détaillée. [#05a842b](https://github.com/betagouv/lab-anssi-ui-kit/commit/05a842b)
- Ajout de la prop 'neutral' au composant DsfrLink pour modifier son apparence. [#c7d38ae](https://github.com/betagouv/lab-anssi-ui-kit/commit/c7d38ae)
- Ajout du composant Notice. [#81b185f](https://github.com/betagouv/lab-anssi-ui-kit/commit/81b185f)
- Ajout de la prop 'hideDetails' au composant DsfrStepper. [#590ce7e](https://github.com/betagouv/lab-anssi-ui-kit/commit/590ce7e)
- Amélioration de la gestion du layout responsive du composant DsfrSegmented. [#670fd88](https://github.com/betagouv/lab-anssi-ui-kit/commit/670fd88)

### Évolutions techniques
- Refactorisation des composants pour utiliser la fonction 'withIconsStyleSheet'. [#1f03fb4](https://github.com/betagouv/lab-anssi-ui-kit/commit/1f03fb4)
- Mise à jour des dépendances : Svelte (v5.55.0), DSFR (v1.14.4), Storybook (v10.3.3), TypeScript (v6.0.2), Vitest (v4.1.1). [#6b96626](https://github.com/betagouv/lab-anssi-ui-kit/commit/6b96626), [#880b624](https://github.com/betagouv/lab-anssi-ui-kit/commit/880b624), [#654d7b0](https://github.com/betagouv/lab-anssi-ui-kit/commit/654d7b0), [#15f4801](https://github.com/betagouv/lab-anssi-ui-kit/commit/15f4801), [#b29cdff](https://github.com/betagouv/lab-anssi-ui-kit/commit/b29cdff)
- Application de patchs de sécurité pour corriger des vulnérabilités détectées par Dependabot. [#c63aaef](https://github.com/betagouv/lab-anssi-ui-kit/commit/c63aaef), [#d88cbe1](https://github.com/betagouv/lab-anssi-ui-kit/commit/d88cbe1), [#5ff3d76](https://github.com/betagouv/lab-anssi-ui-kit/commit/5ff3d76)
- Modification du mixin 'set-shadow-host' pour piloter l'application du 'font-size' dans le composant DsfrLink. [#1d1f2ec](https://github.com/betagouv/lab-anssi-ui-kit/commit/1d1f2ec)
- Amélioration de la gestion de l'attribut 'data-themeable' dans la fonction setThemeable. [#7e79174](https://github.com/betagouv/lab-anssi-ui-kit/commit/7e79174)
- Correction de l'application des props 'fint' et 'radio' sur les éléments radio du composant DsfrRadiosGroup. [#271443a](https://github.com/betagouv/lab-anssi-ui-kit/commit/271443a)

### Autres changements
- Amélioration de la lisibilité des descriptions des slots dans les stories. [#b53a03e](https://github.com/betagouv/lab-anssi-ui-kit/commit/b53a03e) et [#7087728](https://github.com/betagouv/lab-anssi-ui-kit/commit/7087728)
- Ajout de l'attribut 'id' au composant DsfrTag. [#0ead556](https://github.com/betagouv/lab-anssi-ui-kit/commit/0ead556)
- Amélioration du mode de calcul de la hauteur des onglets dans le composant DsfrTabs. [#8f64c67](https://github.com/betagouv/lab-anssi-ui-kit/commit/8f64c67)
- Suppression du bloc de lien "NIS2" dans la suite Cyber. [#6de23ff](https://github.com/betagouv/lab-anssi-ui-kit/commit/6de23ff)
- Revert d'une modification concernant la publication des packages NPM. [#f022064](https://github.com/betagouv/lab-anssi-ui-kit/commit/f022064)
- Mise à jour de la version de la bibliothèque (1.44.8, 1.44.9, 1.45.0, 1.46.0, 1.46.1, 1.46.2, 1.47.0, 1.47.1, 1.47.2). [#9e2defb](https://github.com/betagouv/lab-anssi-ui-kit/commit/9e2defb), [#df89a5e](https://github.com/betagouv/lab-anssi-ui-kit/commit/df89a5e), [#9f18625](https://github.com/betagouv/lab-anssi-ui-kit/commit/9f18625), [#5a22049](https://github.com/betagouv/lab-anssi-ui-kit/commit/5a22049), [#3c66734](https://github.com/betagouv/lab-anssi-ui-kit/commit/3c66734), [#2c438b6](https://github.com/betagouv/lab-anssi-ui-kit/commit/2c438b6), [#6ed8884](https://github.com/betagouv/lab-anssi-ui-kit/commit/6ed8884)
