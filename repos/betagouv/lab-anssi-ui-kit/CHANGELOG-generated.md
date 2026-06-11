## Changelog : lab-anssi-ui-kit (30 derniers jours, au 10 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées au UI Kit du Lab. ANSSI au cours du dernier mois. Les principales évolutions concernent l'ajout de nouvelles fonctionnalités au composant `DsfrTable` (sélection de lignes, pagination, etc.), l'ajout du composant "Bandeau page", ainsi que des améliorations sur les composants `DsfrButton`, `DsfrNavigation`, `DsfrInput`, `DsfrTextarea` et `DsfrCheckbox`. Des corrections de style et des événements personnalisés ont également été ajoutés pour une meilleure interactivité et accessibilité.

### Évolutions fonctionnelles
- Ajout du composant "Bandeau page" ([#c79a246](https://github.com/betagouv/lab-anssi-ui-kit/commit/c79a246)).
- Le composant `DsfrTable` permet désormais de sélectionner des lignes et d'utiliser une fonctionnalité "tout sélectionner" ([#61aec1b](https://github.com/betagouv/lab-anssi-ui-kit/commit/61aec1b)).
- Ajout d'événements personnalisés pour la pagination et le changement du nombre de lignes par page dans `DsfrTable` ([#8588078](https://github.com/betagouv/lab-anssi-ui-kit/commit/8588078)).
- Ajout de la variation "Mega Menu" au composant `DsfrNavigation` avec la possibilité d'insérer des slots ([#2fef22e](https://github.com/betagouv/lab-anssi-ui-kit/commit/2fef22e)).
- Ajout de la propriété `hideLabel` aux composants `DsfrInput` et `DsfrTextarea` pour masquer le label ([#b58269f](https://github.com/betagouv/lab-anssi-ui-kit/commit/b58269f), [#8e974fc](https://github.com/betagouv/lab-anssi-ui-kit/commit/8e974fc)).
- Ajout de la propriété `hideLabel` au composant `DsfrRange` pour masquer le libellé ([#51ab68a](https://github.com/betagouv/lab-anssi-ui-kit/commit/51ab68a)).
- Ajout de la variation 'indeterminate' au composant `DsfrCheckbox` ([#5dcbb87](https://github.com/betagouv/lab-anssi-ui-kit/commit/5dcbb87)).
- Amélioration des stories du composant `DsfrNavigation` ([#2e0b522](https://github.com/betagouv/lab-anssi-ui-kit/commit/2e0b522)).
- Ajout de la prop `noIcon` au composant `DsfrTile` pour masquer l'icône associée au lien ([#9f8339b](https://github.com/betagouv/lab-anssi-ui-kit/commit/9f8339b)).

### Évolutions techniques
- Uniformisation des variations personnalisées des composants `DsfrButton` et `DsfrButtonsGroup` ([#ad7c9e9](https://github.com/betagouv/lab-anssi-ui-kit/commit/ad7c9e9)).
- Ajout de la possibilité de passer une prop 'rich' par colonne dans `DsfrTable` ([#54f571b](https://github.com/betagouv/lab-anssi-ui-kit/commit/54f571b)).
- Nettoyage du code et suppression de fonctionnalités inutilisées dans `DsfrTable` ([#ff4afa7](https://github.com/betagouv/lab-anssi-ui-kit/commit/ff4afa7)).
- Suppression de l'implémentation de la fonctionnalité 'render' propre aux usages Svelte dans `DsfrTable` ([#b5349fa](https://github.com/betagouv/lab-anssi-ui-kit/commit/b5349fa)).
- Uniformisation de la façon de déclarer les CustomEvent dans les composants ([#f515a78](https://github.com/betagouv/lab-anssi-ui-kit/commit/f515a78)).
- Ajout des évènements des composants à la table des arguments des stories ([#19dde81](https://github.com/betagouv/lab-anssi-ui-kit/commit/19dde81)).
- Ajout des URLs de documentation pour chaque composant ([#bbe34cb](https://github.com/betagouv/lab-anssi-ui-kit/commit/bbe34cb)).
- Génération d'un fichier `web-types` pour améliorer l'autocomplétion dans les éditeurs de code ([#0e507e7](https://github.com/betagouv/lab-anssi-ui-kit/commit/0e507e7), [#ff45203](https://github.com/betagouv/lab-anssi-ui-kit/commit/ff45203)).
- Ajout des évènements émis par les composants dans le fichier `web-types` ([#a128d61](https://github.com/betagouv/lab-anssi-ui-kit/commit/a128d61)).
- Ajout des types réels des props ([#24631b2](https://github.com/betagouv/lab-anssi-ui-kit/commit/24631b2)).
- Ajout de la propriété 'lab-border-radius' comme thématisable ([#014010f](https://github.com/betagouv/lab-anssi-ui-kit/commit/014010f)).

### Autres changements
- Génération d'un manifest des composants ([#b7286a9](https://github.com/betagouv/lab-anssi-ui-kit/commit/b7286a9)).
- Documentation des slots dans le manifest ([#21f8ced](https://github.com/betagouv/lab-anssi-ui-kit/commit/21f8ced)).
- Correction de l'affichage du caption dans `DsfrTable` ([#96dc229](https://github.com/betagouv/lab-anssi-ui-kit/commit/96dc229)).
- Correction du style pour les cases à cocher 'checked' et 'indeterminate' dans `DsfrCheckbox` ([#0212aca](https://github.com/betagouv/lab-anssi-ui-kit/commit/0212aca)).
- Mise à jour des dépendances ([#3e20e50](https://github.com/betagouv/lab-anssi-ui-kit/commit/3e20e50), [#87cd2be](https://github.com/betagouv/lab-anssi-ui-kit/commit/87cd2be)).
- Ajout du dossier statique pour Storybook ([#f3fc93e](https://github.com/betagouv/lab-anssi-ui-kit/commit/f3fc93e)).
- Correction pour forcer la création du dossier `/dist` s'il n'existe pas ([#4702564](https://github.com/betagouv/lab-anssi-ui-kit/commit/4702564)).
- Autorisation du "trusted publishing" sur NPM ([#46e2054](https://github.com/betagouv/lab-anssi-ui-kit/commit/46e2054)).
- Bump de la version de Playwright ([#f85784f](https://github.com/betagouv/lab-anssi-ui-kit/commit/f85784f)).
- Eviter de télécharger plusieurs navigateurs Playwright ([#9458cb4](https://github.com/betagouv/lab-anssi-ui-kit/commit/9458cb4)).
