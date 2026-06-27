## Changelog : fondation (30 derniers jours, au 2026-06-25)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'interface utilisateur, notamment au niveau de la gestion des agendas et des fichiers, ainsi que sur la migration vers une nouvelle architecture frontale plus modulaire et maintenable. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de la sélection des fichiers d'agenda et ajout de la possibilité de verrouiller les fichiers une fois qu'ils sont officiellement rapportés. [#384](https://github.com/betagouv/fondation/issues/384)
- Possibilité d'ajouter des pièces jointes aux dossiers de nomination. [#407](https://github.com/betagouv/fondation/issues/407)
- Ajout de la possibilité de renoncer à des présentations de plans. [#378](https://github.com/betagouv/fondation/issues/378)
- Amélioration de l'affichage des informations sur les sessions, notamment l'heure de fin dans les rapports officiels. [#379](https://github.com/betagouv/fondation/issues/379)
- Remplacement du modal de magistrat par un panneau latéral pour une meilleure expérience utilisateur. [#439](https://github.com/betagouv/fondation/issues/439)
- Amélioration de l'affichage des plans avec la possibilité de trier les membres par ordre de protocole. [#384](https://github.com/betagouv/fondation/issues/384)
- Ajout de la possibilité de filtrer les fichiers déjà rapportés dans l'agenda. [#397](https://github.com/betagouv/fondation/issues/397)

### Évolutions techniques
- Migration vers Vitest pour les tests unitaires. [#437](https://github.com/betagouv/fondation/issues/437)
- Refactoring de plusieurs modules (admin, reports, summary, auth, shared) vers une architecture frontale basée sur des "features" pour une meilleure organisation et maintenabilité. [#426](https://github.com/betagouv/fondation/issues/426), [#427](https://github.com/betagouv/fondation/issues/427), [#428](https://github.com/betagouv/fondation/issues/428), [#429](https://github.com/betagouv/fondation/issues/429), [#430](https://github.com/betagouv/fondation/issues/430), [#431](https://github.com/betagouv/fondation/issues/431), [#432](https://github.com/betagouv/fondation/issues/432), [#433](https://github.com/betagouv/fondation/issues/433)
- Utilisation de tokens de couleurs DSFR au lieu des couleurs Tailwind natives. [#418](https://github.com/betagouv/fondation/issues/418)
- Suppression de packages `shared-models` inutilisés. [#426](https://github.com/betagouv/fondation/issues/426)
- Mise à jour de plusieurs dépendances (piscina, react-router, vite, react monorepo) pour corriger des failles de sécurité et bénéficier des dernières améliorations. [#422](https://github.com/betagouv/fondation/issues/422), [#423](https://github.com/betagouv/fondation/issues/423), [#435](https://github.com/betagouv/fondation/issues/435)
- Utilisation de SheetJS pour la gestion des fichiers Excel.

### Autres changements
- Ajout d'une documentation pour l'architecture frontale "feature-first". [#434](https://github.com/betagouv/fondation/issues/434)
- Amélioration de la configuration du CI/CD pour éviter les limites de mémoire de Renovate. [#420](https://github.com/betagouv/fondation/issues/420)
- Correction de plusieurs bugs mineurs liés à l'affichage et à la gestion des données.
- Mise à jour de la documentation et des tests.
- Amélioration de la gestion des priorités. [#414](https://github.com/betagouv/fondation/issues/414)
- Ajout de tests pour la documentation. [#399](https://github.com/betagouv/fondation/issues/399)
