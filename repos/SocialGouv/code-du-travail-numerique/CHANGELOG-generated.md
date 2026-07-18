## Changelog : code-du-travail-numerique (30 derniers jours, au 2026-07-16)

### Résumé
Les dernières mises à jour apportent des corrections de bugs, des améliorations de l'expérience utilisateur, notamment concernant la recherche d'entreprises et la notation des contributions, ainsi que des optimisations techniques pour la gestion des accords et le processus de release. Un nouveau système d'extraction d'événements pour le suivi analytique a également été implémenté.

### Évolutions fonctionnelles
- Ajout d'un widget de notation pour les contributions, permettant aux utilisateurs de donner leur avis. [#7344](https://github.com/SocialGouv/code-du-travail-numerique/issues/7344)
- Amélioration de la recherche d'entreprise : découplage de l'affichage des accords de la recherche. [#7324](https://github.com/SocialGouv/code-du-travail-numerique/issues/7324)
- Correction d'un bug empêchant l'affichage correct des entêtes de tableaux dans les contributions. [#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325)
- Suppression de la sélection de convention collective dans l'en-tête. [#7388](https://github.com/SocialGouv/code-du-travail-numerique/issues/7388)
- Correction de l'affichage du code IDCC 9999 pour une normalisation. [#7303](https://github.com/SocialGouv/code-du-travail-numerique/issues/7303)
- Redirection de l'ancienne fiche canicule vers la nouvelle page d'information. [#7318](https://github.com/SocialGouv/code-du-travail-numerique/issues/7318)
- Ajout du type "bon à savoir" pour les contributions. [#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326)

### Évolutions techniques
- Utilisation des accords dans l'ES (Elasticsearch) au lieu de l'API Legifrance pour améliorer les performances et la fiabilité. [#7381](https://github.com/SocialGouv/code-du-travail-numerique/issues/7381)
- Mise en place d'un système d'extraction d'événements statiques et de vérification de la dérive pour le suivi analytique. [#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300)
- Migration des builds d'images de buildkit-service vers buildkit-operator. [#7354](https://github.com/SocialGouv/code-du-travail-numerique/issues/7354)
- Désactivation de Husky lors d'une release pour éviter des problèmes de build.
- Mise à jour de pnpm vers la version 11.
- Correction de bugs liés au passage à pnpm 11.

### Autres changements
- Ajout du `user-agent` pour que les données de notation soient correctement remontées dans Matomo. [#7390](https://github.com/SocialGouv/code-du-travail-numerique/issues/7390)
- Correction du focus sur les résultats lors de la recherche automatique. [#7391](https://github.com/SocialGouv/code-du-travail-numerique/issues/7391)
- Fin de l'A/B test concernant les contributions (CC) et conservation de la version 3 avec boutons radio. [#7379](https://github.com/SocialGouv/code-du-travail-numerique/issues/7379)
- Correction de niveaux de titres incorrects dans la section actualités.
- Ajout de logs pour la recherche DILA afin de faciliter le débogage.
- Mise à jour des secrets pour l'environnement de préproduction.
- Suppression de la balise canonical sur la page générique des contributions. [#7316](https://github.com/SocialGouv/code-du-travail-numerique/issues/7316)
- Correction des tests E2E pour le glossaire, la recherche dans l'en-tête et les conventions collectives. [#7319](https://github.com/SocialGouv/code-du-travail-numerique/issues/7319)
