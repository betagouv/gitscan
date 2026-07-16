## Changelog : code-du-travail-numerique (30 derniers jours, au 2026-07-15)

### Résumé
Les dernières mises à jour apportent des corrections de bugs, notamment sur l'affichage des accords et des tableaux, ainsi que des améliorations concernant la recherche DILA et la gestion des contributions. De nouvelles fonctionnalités ont été ajoutées, comme un widget de notation des contributions et un système d'extraction d'événements pour le suivi analytique. L'infrastructure a également été mise à jour avec un passage à pnpm 11 et une migration des builds d'images Docker.

### Évolutions fonctionnelles
- Ajout d'un widget de notation pour les contributions [#7344](https://github.com/SocialGouv/code-du-travail-numerique/issues/7344).
- Amélioration de la recherche d'entreprise et découplage de l'affichage des accords [#7324](https://github.com/SocialGouv/code-du-travail-numerique/issues/7324).
- Ajout du type "bon à savoir" pour les contributions [#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326).
- Correction d'un bug empêchant l'affichage correct des entêtes de tableaux dans les contributions [#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325).
- Correction d'un problème avec l'ancre des accordéons dans les tests E2E.
- Correction d'un bug lié au bouton de fermeture du mode plein écran sur les tableaux de contributions [#7373](https://github.com/SocialGouv/code-du-travail-numerique/issues/7373).
- Redirection de l'ancienne fiche canicule vers la nouvelle page d'information [#7318](https://github.com/SocialGouv/code-du-travail-numerique/issues/7318) et [#7322](https://github.com/SocialGouv/code-du-travail-numerique/issues/7322).
- Normalisation de l'affichage du code IDCC 9999 pour les conventions collectives [#7303](https://github.com/SocialGouv/code-du-travail-numerique/issues/7303).

### Évolutions techniques
- Migration des builds d'images Docker de buildkit-service vers buildkit-operator [#7354](https://github.com/SocialGouv/code-du-travail-numerique/issues/7354).
- Mise à jour de pnpm.
- Ajout d'un système d'extraction d'événements statiques et de vérification de la dérive des événements [#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300).
- Utilisation des accords dans l'ES au lieu de l'API Legifrance [#7381](https://github.com/SocialGouv/code-du-travail-numerique/issues/7381).
- Génération de la documentation du plan de suivi à partir des événements [#7343](https://github.com/SocialGouv/code-du-travail-numerique/issues/7343).

### Autres changements
- Désactivation de Husky lors d'une release.
- Mise à jour des secrets pour la preprod.
- Ajout de logs sur la recherche DILA.
- Suppression de la balise canonical sur la page générique des contributions [#7316](https://github.com/SocialGouv/code-du-travail-numerique/issues/7316).
