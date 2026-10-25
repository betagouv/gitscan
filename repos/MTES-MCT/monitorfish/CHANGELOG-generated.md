## Changelog : monitorfish (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois-ci, monitorfish a progressé sur l'amélioration de l'expérience utilisateur et la fiabilité des données métier. Les agents bénéficient de nouveaux outils d'exportation de données (CSV), d'une meilleure visibilité sur les informations manquantes lors des contrôles, et d'une gestion plus fine des signalements. L'interface a également été modernisée pour respecter les standards d'accessibilité (DSFR) et la cartographie est désormais plus fluide lors des déplacements autour du globe.

### Évolutions fonctionnelles

**Signalements et Alertes**
- Amélioration de l'exportation des signalements en format CSV avec l'ajout des coordonnées géographiques [#5586](https://github.com/MTES-MCT/monitorfish/issues/5586).
- Possibilité de consulter les signalements archivés directement dans la vue liste [#5536](https://github.com/MTES-MCT/monitorfish/issues/5536).
- Ajout du type de cible "Engin" dans les formulaires de signalement INN [#5305](https://github.com/MTES-MCT/monitorfish/issues/5305).
- Archivage automatique des signalements de navires ne contenant pas de photo (JPEG) [#5562](https://github.com/MTES-MCT/monitorfish/issues/5562).
- Mise en place de nouveaux types d'alertes liés aux dysfonctionnements de balises et à l'activité déclarée [#d300e666](https://github.com/MTES-MCT/monitorfish/commit/d300e666).

**Gestion des contrôles et missions**
- Amélioration de la visibilité des champs manquants lors des contrôles (mise en évidence et info-bulles) [#5507](https://github.com/MTES-MCT/monitorfish/issues/5507).
- Affichage des contrôles croisés directement sur la fiche navire [#5579](https://github.com/MTES-MCT/monitorfish/issues/5579).
- Affinement des règles de saisie pour les missions (gestion du maillage et des engins de pêche) [#f33d6367](https://github.com/MTES-MCT/monitorfish/commit/f33d6367).
- Masquage automatique du champ "Last haul" pour certains types d'engins de pêche spécifiques [#5559](https://github.com/MTES-MCT/monitorfish/issues/5559).

**Cartographie et Navigation**
- Correction du comportement de la carte lors du passage de l'antiméridien pour permettre un tour du globe fluide [#5571](https://github.com/MTES-MCT/monitorfish/issues/5571).
- Sauvegarde de l'organisation des couches cartographiques par profil utilisateur [#5501](https://github.com/MTES-MCT/monitorfish/issues/5501).

**Interface et Accessibilité**
- Mise en conformité de la page de connexion avec le design système DSFR [#5548](https://github.com/MTES-MCT/monitorfish/issues/5548).
- Ajout d'une page de déclaration d'accessibilité accessible depuis la connexion [#5553](https://github.com/MTES-MCT/monitorfish/issues/5553).
- Ajout d'un filtre "Équipé VMS" dans la liste des navires [#5500](https://github.com/MTES-MCT/monitorfish/issues/5500).

### Évolutions techniques

**Frontend et Tests**
- Migration vers TypeScript 7 pour l'ensemble du frontend [#3e47ed28](https://github.com/MTES-MCT/monitorfish/commit/3e47ed28).
- Migration de l'outil de tests E2E vers Cypress 16 [#e481cb1e](https://github.com/MTES-MCT/monitorfish/commit/e481cb1e).
- Résolution de plusieurs tests instables (flaky tests) pour stabiliser la CI [#1e57b231](https://github.com/MTES-MCT/monitorfish/commit/1e57b231).

**Backend et Observabilité**
- Amélioration du monitoring avec l'envoi automatique des erreurs de flux (Prefect) vers Sentry [#5538](https://github.com/MTES-MCT/monitorfish/issues/5538).
- Création d'un package dédié aux types d'API pour assurer la cohérence des données entre le backend et RapportNav [#5546](https://github.com/MTES-MCT/monitorfish/issues/5546).

**Intégration**
- Remplacement de l'outil de chat par une intégration via webhook Tchap [#5514](https://github.com/MTES-MCT/monitorfish/issues/5514).

### Autres changements
- Mise à jour de la documentation de l'application et technique [#5527](https://github.com/MTES-MCT/monitorfish/issues/5527).
- Ajout de plusieurs documents d'architecture (ADRs) pour documenter les décisions techniques importantes [#4fc0b593](https://github.com/MTES-MCT/monitorfish/commit/4fc0b593).
