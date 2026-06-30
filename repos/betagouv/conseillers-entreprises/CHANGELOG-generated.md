## Changelog : conseillers-entreprises (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration des modèles d'emails de sollicitation, l'ajout de statistiques plus précises et la modernisation de l'infrastructure technique. Des améliorations de l'interface utilisateur et des corrections de bugs ont également été apportées pour une meilleure expérience globale.

### Évolutions fonctionnelles
- **Statistiques :** Ajout d'une colonne "Évolution" dans le rapport des coopérations pour visualiser les changements. [#4500](https://github.com/betagouv/conseillers-entreprises/pull/4500)
- **Statistiques :** Possibilité de générer des rapports statistiques directement depuis l'interface d'administration. [#4498](https://github.com/betagouv/conseillers-entreprises/pull/4498)
- **Emails de sollicitation :** Refonte complète de la gestion des modèles d'emails de sollicitation :
    - Ajout d'un modèle `SolicitationMailTemplate` avec validation et interface d'administration. [#4485](https://github.com/betagouv/conseillers-entreprises/pull/4485)
    - Possibilité de définir un ordre pour les modèles d'emails.
    - Amélioration de l'interface d'administration pour la gestion des modèles.
    - Remplacement du contenu statique des emails par du HTML dynamique provenant des modèles.
    - Gestion améliorée des cas d'absence de modèle pour certains types d'emails.
- **Temoignages d'experts :** Ajout d'une section "Témoignages d'experts" sur le site, avec une structure et un contenu mis à jour. [#4506](https://github.com/betagouv/conseillers-entreprises/pull/4506)
- **Équipe :** Mise à jour de la page "Équipe" avec des ajustements. [#4513](https://github.com/betagouv/conseillers-entreprises/pull/4513)

### Évolutions techniques
- **Migration vers esbuild :** Remplacement de webpack par esbuild pour l'optimisation des assets, améliorant ainsi les performances et la maintenance. [#4520](https://github.com/betagouv/conseillers-entreprises/pull/4520)
- **Suppression de jQuery :** Suppression de la dépendance à jQuery et remplacement par des alternatives modernes. [#4542](https://github.com/betagouv/conseillers-entreprises/pull/4542)
- **Optimisation du code :** Simplification et refactoring de plusieurs classes et méthodes, notamment dans les services liés à la gestion du temps et des rapports. [#4519](https://github.com/betagouv/conseillers-entreprises/pull/4519), [#4494](https://github.com/betagouv/conseillers-entreprises/pull/4494)
- **Mise à jour des dépendances :** Mises à jour de plusieurs dépendances (Ruby, Nokogiri, net-imap, undici, concurrent-ruby) pour bénéficier des dernières corrections de sécurité et améliorations de performances.
- **Configuration :** Amélioration de la configuration de CircleCI et ajout de caches pour accélérer les builds.
- **Base de données :** Correction des valeurs de timeout de la base de données. [#4537](https://github.com/betagouv/conseillers-entreprises/pull/4537)

### Autres changements
- **Documentation :** Mise à jour de la documentation de l'architecture du projet. [#4463](https://github.com/betagouv/conseillers-entreprises/pull/4463)
- **Tests :** Ajout et mise à jour de tests unitaires et d'intégration.
- **Corrections de bugs :** Correction de plusieurs bugs mineurs, notamment liés à l'affichage des dates et à la gestion des erreurs.
- **Nettoyage du code :** Suppression de code inutilisé et amélioration de la lisibilité du code.
- **Amélioration de l'interface d'administration :** Réduction du nombre d'éléments affichés par page dans l'interface d'administration. [#4525](https://github.com/betagouv/conseillers-entreprises/pull/4525)
