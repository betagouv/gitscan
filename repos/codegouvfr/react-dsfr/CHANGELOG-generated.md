## Changelog : react-dsfr (30 derniers jours, au 31 août 2026)

### Résumé
Les récentes évolutions se concentrent sur une optimisation majeure des performances permettant de réduire le poids du CSS chargé par les utilisateurs. L'accessibilité a également été renforcée, notamment pour les composants d'alerte, et plusieurs corrections de bugs ont été apportées sur les formulaires et les menus pour garantir une interface plus stable.

### Évolutions fonctionnelles
- **Accessibilité** : Amélioration du composant Alert, dont le rôle ARIA est désormais défini dynamiquement en fonction de son niveau de sévérité [#503](https://github.com/codegouvfr/react-dsfr/pull/503).
- **Correction d'interface** :
    - Correction des classes CSS des messages dans les champs de saisie (Input) [#492](https://github.com/codegouvfr/react-dsfr/pull/492).
    - Correction du composant Footer pour permettre l'utilisation de ReactNode dans les noms de catégories [#493](https://github.com/codegouvfr/react-dsfr/pull/493).
    - Correction du type de bouton au sein du menu latéral (Side Menu) [#501](https://github.com/codegouvfr/react-dsfr/pull/501).

### Évolutions techniques
- **Optimisation de la performance** : Introduction d'une nouvelle fonctionnalité permettant de ne charger que le CSS des composants réellement utilisés (`only-include-used-components`), réduisant ainsi l'empreinte CSS du projet [#505](https://github.com/codegouvfr/react-dsfr/pull/505).
- **Refactoring** : Refonte de l'API externe liée à l'optimisation du CSS pour une meilleure utilisation [#505](https://github.com/codegouvfr/react-dsfr/pull/505).
- **Amélioration de la détection** : Correction de l'algorithme de détection de contenu pour éviter l'inclusion excessive de styles non nécessaires [#515](https://github.com/codegouvfr/react-dsfr/pull/515).
- **CI/CD & Infrastructure** :
    - Correction du job de publication sur npm dans la chaîne de CI [#507](https://github.com/codegouvfr/react-dsfr/pull/507).
    - Amélioration de la robustesse du processus de build en gérant l'absence du fichier `index.html` [#506](https://github.com/codegouvfr/react-dsfr/pull/506).
