## Changelog : referentiel-applications (30 derniers jours, au 31 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'accessibilité, la gestion des données et l'expérience utilisateur. Des correctifs ont été implémentés pour améliorer la stabilité et la fiabilité de l'application, notamment au niveau des tests et de la gestion de la base de données. De nouvelles fonctionnalités ont été ajoutées pour la gestion des divisions métiers et l'affichage des informations techniques des applications.

### Évolutions fonctionnelles
- Ajout d'un mode de maintenance en lecture seule pour l'application ([#2201](https://github.com/dnum-mi/referentiel-applications/issues/2201)).
- Normalisation des tags en minuscules pour une meilleure cohérence des données ([#2202](https://github.com/dnum-mi/referentiel-applications/issues/2202)).
- Mise à jour de l'affichage de la version de l'application sans rafraîchissement complet de la page ([#2158](https://github.com/dnum-mi/referentiel-applications/issues/2158)).
- Ajout de la possibilité de gérer plusieurs divisions métiers ([#2114](https://github.com/dnum-mi/referentiel-applications/issues/2114)).
- Amélioration de la recherche globale avec préfixe et correction de la fiabilité ([#2025](https://github.com/dnum-mi/referentiel-applications/issues/2025)).
- Affichage du libellé de statut même sans date associée ([#2017](https://github.com/dnum-mi/referentiel-applications/issues/2017)).
- Ajout de l'affichage de la pile technique et des licences sur la fiche d'application ([#1099](https://github.com/dnum-mi/referentiel-applications/issues/1099)).
- Ajout de l'affichage du taux de conformité RGAA et de la date de déclaration d'accessibilité ([#1935](https://github.com/dnum-mi/referentiel-applications/issues/1935)).

### Évolutions techniques
- Migration vers NestJS 11 ([#1937](https://github.com/dnum-mi/referentiel-applications/issues/1937), [#2153](https://github.com/dnum-mi/referentiel-applications/issues/2153)).
- Correction de problèmes de pollution de la base de données de développement par les tests ([#2117](https://github.com/dnum-mi/referentiel-applications/issues/2117)).
- Amélioration de la performance de la recherche d'applications ([#1975](https://github.com/dnum-mi/referentiel-applications/issues/1975)).
- Fiabilisation du démarrage de la base de données et du backend en CI ([#2023](https://github.com/dnum-mi/referentiel-applications/issues/2023)).
- Correction de plusieurs vulnérabilités de sécurité identifiées par Dependabot.
- Suppression de la fonctionnalité de gestion des licences.

### Autres changements
- Amélioration de l'accessibilité (RGAA) : corrections de contraste, champs liés, messages d'état, transcriptions de graphiques, liens explicites, structure globale de la page.
- Documentation du RefApp et des ADR (Architecture Decision Records).
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour des dépendances.
