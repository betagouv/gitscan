## Changelog : mon-entreprise (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la modernisation de l'infrastructure du projet avec le passage à Next.js 16 et une refonte complète des workflows GitHub Actions. Des corrections de calculs pour l'auto-entrepreneur et des mises à jour des données (plafonds de CA) ont également été apportées. Enfin, le simulateur RGCP a été décommissionné.

### Évolutions fonctionnelles
- Décommissionnement du simulateur RGCP et suppression des règles associées dans le modèle social. [#1234](https://github.com/betagouv/mon-entreprise/issues/1234)
- Correction du calcul de l'IR pour les auto-entrepreneurs. [#4105](https://github.com/betagouv/mon-entreprise/issues/4105)
- Mise à jour des plafonds de chiffre d'affaires (CA) pour l'auto-entreprise.
- Correction d'un problème de FOUC (Flash Of Unstyled Content) causé par l'utilisation de `navigator` dans un environnement Node.js.

### Évolutions techniques
- Migration vers Next.js 16 avec implémentation de l'internationalisation (i18n) côté serveur (SSR). [#4215](https://github.com/betagouv/mon-entreprise/issues/4215)
- Refonte complète des workflows GitHub Actions pour améliorer la gestion des CI/CD, incluant la séparation des tests E2E de production et la gestion des secrets.
- Amélioration de l'isolation du téléchargement d'artefacts pour CodeQL.
- Passage des workflows de publication et de vérification sur un modèle export/push.
- Correction de références de workflow brisées.
- Mise à jour des versions de Node.js dans `flake.nix`, `.nvmrc` et `package.json`.
- Refactoring du code Algolia pour une meilleure organisation.
- Correction de la gestion des erreurs dans le script de nettoyage Algolia.

### Autres changements
- Traduction de la page d'accueil "hello world".
- Ajout de la gestion des warnings CodeQL sur le checkout de références non vérifiées.
- Corrections de formatage Prettier et mises à jour des traductions i18n.
- Restauration d'une traduction manquante pour le JEI dans les règles i18n.
- Suppression de règles inutiles dans le modèle AS.
- Déplacement de composants de réduction vers lodeom.
- Remplacement de chemins relatifs par des alias `@/`.
- Correction d'un bug dans le tracking Piano Analytics qui envoyait des erreurs Sentry.
- Correction d'un problème de syntaxe dans la configuration des secrets GitHub Actions.
