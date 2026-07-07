## Changelog : data_pass (30 derniers jours, au 06 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la sécurité (durcissement de la session, gestion des clés API), des corrections de bugs et des évolutions fonctionnelles pour faciliter l'administration des autorisations et l'intégration avec d'autres services (HubEE, CNOUS). L'expérience utilisateur a également été améliorée grâce à des optimisations de la recherche et de l'affichage des données.

### Évolutions fonctionnelles
- Ajout de la démarche DDMariage au formulaire HubEE DILA. (PR [#1667](https://github.com/etalab/data_pass/pull/1667))
- Amélioration de la recherche d'utilisateurs et de la gestion des droits. (PR [#1608](https://github.com/etalab/data_pass/pull/1608), [#1625](https://github.com/etalab/data_pass/pull/1625))
- Possibilité pour les managers d'attribuer le rôle développeur à leurs utilisateurs. (PR [#1618](https://github.com/etalab/data_pass/pull/1618))
- Ajout d'une fonctionnalité de désinscription en un clic depuis un email. (PR [#1606](https://github.com/etalab/data_pass/pull/1606))
- Affichage des demandes validées dans les résultats de recherche par ID. (PR [#1602](https://github.com/etalab/data_pass/pull/1602))
- Intégration de la gestion des communes CNOUS avec affichage client-side du périmètre géographique. (PR [#1584](https://github.com/etalab/data_pass/pull/1584), [#1626](https://github.com/etalab/data_pass/pull/1626))
- Amélioration des wordings pour le cas d'usage EAJE pour l'API particulier. (PR [#1647](https://github.com/etalab/data_pass/pull/1647))
- Mise à jour des liens vers les CGU des services CISIRH. (PR [#1617](https://github.com/etalab/data_pass/pull/1617), [#1621](https://github.com/etalab/data_pass/pull/1621))
- Ajout de la possibilité de définir plusieurs templates de cas d'usage pour un même formulaire. (PR [#1612](https://github.com/etalab/data_pass/pull/1612))

### Évolutions techniques
- Durcissement de la session à 12 heures fixes. (PR [#1657](https://github.com/etalab/data_pass/pull/1657))
- Mise en place d'un module de gestion des *feature flags* centralisé. (PR [#1656](https://github.com/etalab/data_pass/pull/1656))
- Migration du scope TVA d'API Entreprise de VIES vers la DGFIP. (PR [#1622](https://github.com/etalab/data_pass/pull/1622))
- Refactoring du code pour améliorer la performance et la maintenabilité (plusieurs PRs).
- Correction d'une fuite mémoire potentielle dans les alertes utilisateur. (PR [#1656](https://github.com/etalab/data_pass/pull/1656))
- Correction d'un problème de suppression de lignes de droits utilisateur. (PR [#1634](https://github.com/etalab/data_pass/pull/1634))
- Correction d'un problème de restauration d'autorisation. (PR [#1655](https://github.com/etalab/data_pass/pull/1655))

### Autres changements
- Documentation de l'authentification ProConnect. (PR [#1622](https://github.com/etalab/data_pass/pull/1622))
- Mise à jour des dépendances (Rubocop, Yard, Faraday, etc.).
- Amélioration de la documentation et des tests.
- Nettoyage du code et refactoring de certains composants.
- Ajout de tests pour les nouvelles fonctionnalités.
