## Changelog : lab-anssi-ui-kit (30 derniers jours, au 5 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées au UI Kit du Lab. ANSSI au cours du dernier mois. Les principales évolutions concernent l'ajout de nouvelles fonctionnalités aux composants existants, notamment pour les tableaux (sélection de lignes, pagination, etc.) et la navigation (menus "Mega Menu"). Des améliorations ont également été apportées à la documentation et à la gestion des événements, rendant les composants plus flexibles et plus faciles à utiliser.

### Évolutions fonctionnelles
- Ajout du composant "Bandeau page" [#c79a246](https://github.com/betagouv/lab-anssi-ui-kit/commit/c79a246).
- Amélioration du composant `DsfrNavigation` avec l'ajout de la variation "Mega Menu" et la possibilité d'insérer des slots dans ces menus [#2fef22e](https://github.com/betagouv/lab-anssi-ui-kit/commit/2fef22e).
- Ajout de la variation 'selectable' au composant `DsfrTable`, permettant la sélection de lignes [#61aec1b](https://github.com/betagouv/lab-anssi-ui-kit/commit/61aec1b).
- Implémentation de la fonctionnalité "tout sélectionner" pour la sélection des lignes dans le composant `DsfrTable` [#21a3221](https://github.com/betagouv/lab-anssi-ui-kit/commit/21a3221).
- Ajout de la propriété `hideLabel` aux composants `DsfrInput` et `DsfrTextarea` pour masquer le label [#b58269f](https://github.com/betagouv/lab-anssi-ui-kit/commit/b58269f).
- Ajout de la propriété `hideLabel` au composant `DsfrRange` pour masquer le libellé [#51ab68a](https://github.com/betagouv/lab-anssi-ui-kit/commit/51ab68a).
- Ajout de la variation 'indeterminate' au composant `DsfrCheckbox` [#5dcbb87](https://github.com/betagouv/lab-anssi-ui-kit/commit/5dcbb87).

### Évolutions techniques
- Uniformisation de la façon de déclarer les `CustomEvent` dans les composants [#f515a78](https://github.com/betagouv/lab-anssi-ui-kit/commit/f515a78).
- Ajout d'un fichier `web-types` pour améliorer l'autocomplétion et la validation dans les éditeurs de code [#0e507e7](https://github.com/betagouv/lab-anssi-ui-kit/commit/0e507e7).
- Génération d'un manifest des composants pour faciliter leur intégration [#b7286a9](https://github.com/betagouv/lab-anssi-ui-kit/commit/b7286a9).
- Ajout des URLs de documentation pour chaque composant [#bbe34cb](https://github.com/betagouv/lab-anssi-ui-kit/commit/bbe34cb).
- Amélioration de la documentation du composant `DsfrTable` et des stories associées [#5dca978](https://github.com/betagouv/lab-anssi-ui-kit/commit/5dca978).
- Nettoyage du code et suppression de fonctionnalités inutilisées dans le composant `DsfrTable` [#ff4afa7](https://github.com/betagouv/lab-anssi-ui-kit/commit/ff4afa7).
- Suppression de l'implémentation de la fonctionnalité 'render' propre aux usages Svelte dans le composant `DsfrTable` [#b5349fa](https://github.com/betagouv/lab-anssi-ui-kit/commit/b5349fa).
- Ajout des événements émis par les composants en tant qu'attributs des éléments [#a128d61](https://github.com/betagouv/lab-anssi-ui-kit/commit/a128d61).
- Ajout des types réels des props [#24631b2](https://github.com/betagouv/lab-anssi-ui-kit/commit/24631b2).
- Uniformisation des variations personnalisées des `DsfrButton` [#ad7c9e9](https://github.com/betagouv/lab-anssi-ui-kit/commit/ad7c9e9).
- Ajout de la propriété 'lab-border-radius' comme thématisable [#014010f](https://github.com/betagouv/lab-anssi-ui-kit/commit/014010f).
- Correction de l'affichage du caption dans le composant `DsfrTable` [#96dc229](https://github.com/betagouv/lab-anssi-ui-kit/commit/96dc229).
- Ajout de CustomEvent pour les changements de page et de lignes par page dans le composant `DsfrTable` [#8588078](https://github.com/betagouv/lab-anssi-ui-kit/commit/8588078).
- Renommage des noms des événements dans un souci de cohérence [#6fe796e](https://github.com/betagouv/lab-anssi-ui-kit/commit/6fe796e).
- Ajout de la possibilité de passer une prop 'rich' par column dans le composant `DsfrTable` [#54f571b](https://github.com/betagouv/lab-anssi-ui-kit/commit/54f571b).

### Autres changements
- Ajout des évènements des composants à la table des arguments des stories dans Storybook [#19dde81](https://github.com/betagouv/lab-anssi-ui-kit/commit/19dde81).
- Ajout de la déclaration du dossier statique pour Storybook [#f3fc93e](https://github.com/betagouv/lab-anssi-ui-kit/commit/f3fc93e).
- Correction pour forcer la création du dossier `/dist` s'il n'existe pas [#4702564](https://github.com/betagouv/lab-anssi-ui-kit/commit/4702564).
- Documentation des slots dans le manifest [#21f8ced](https://github.com/betagouv/lab-anssi-ui-kit/commit/21f8ced).
- Mises à jour de version (1.50.2, 1.51.0, 1.51.1, 1.51.2, 1.52.0, 1.52.1) [#5dcbb87](https://github.com/betagouv/lab-anssi-ui-kit/commit/5dcbb87), [#6e7e562](https://github.com/betagouv/lab-anssi-ui-kit/commit/6e7e562), [#d7624cc](https://github.com/betagouv/lab-anssi-ui-kit/commit/d7624cc), [#cab393a](https://github.com/betagouv/lab-anssi-ui-kit/commit/cab393a), [#1650032](https://github.com/betagouv/lab-anssi-ui-kit/commit/1650032), [#46e2054](https://github.com/betagouv/lab-anssi-ui-kit/commit/46e2054).
- Correction du style pour les cases à cocher 'checked' et 'indeterminate' dans le composant `DsfrCheckbox` [#0212aca](https://github.com/betagouv/lab-anssi-ui-kit/commit/0212aca).
- Autorisation du "trusted publishing" sur NPM [#46e2054](https://github.com/betagouv/lab-anssi-ui-kit/commit/46e2054).
- Bump de la version de Playwright [#f85784f](https://github.com/betagouv/lab-anssi-ui-kit/commit/f85784f).
- Eviter de télécharger plusieurs navigateurs Playwright [#9458cb4](https://github.com/betagouv/lab-anssi-ui-kit/commit/9458cb4).
- Mise à jour des dépendances obsolètes [#87cd2be](https://github.com/betagouv/lab-anssi-ui-kit/commit/87cd2be).
