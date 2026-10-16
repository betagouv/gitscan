## Changelog : monitorfish (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience de contrôle sur le terrain et la précision des signalements. L'outil est devenu plus intuitif pour la gestion des missions et des inspections, tout en offrant une meilleure gestion des alertes liées aux équipements de communication (balises) et une personnalisation accrue de la cartographie pour les utilisateurs.

### Évolutions fonctionnelles
- **Gestion des inspections et contrôles** : 
    - Affichage des contrôles croisés directement sur la fiche navire [#5558](https://github.com/MTES-MCT/monitorfish/issues/5558).
    - Amélioration des formulaires de mission : meilleure visibilité des champs obligatoires, ajout de bulles d'aide (tooltips) et gestion plus fine des champs à choix multiples.
    - Identification facilitée des données manquantes lors des contrôles.
- **Signalements INN (Pêche Illicite, Non déclarée et Non réglementée)** :
    - Ajout de nouveaux types de cibles (Engin, FAD) dans les formulaires de signalement [#5305](https://github.com/MTES-MCT/monitorfish/issues/5305).
    - Possibilité de consulter les signalements archivés dans la vue liste [#5536](https://github.com/MTES-MCT/monitorfish/issues/5536), [#5442](https://github.com/MTES-MCT/monitorfish/issues/5442).
- **Cartographie et Navigation** :
    - Sauvegarde de l'organisation des couches cartographiques au niveau du profil utilisateur [#5501](https://github.com/MTES-MCT/monitorfish/issues/5501).
    - Ajout d'un filtre "Équipé VMS" dans la liste des navires [#5500](https://github.com/MTES-MCT/monitorfish/issues/5500), [#5483](https://github.com/MTES-MCT/monitorfish/issues/5483).
    - Amélioration des filtres de zones sur la carte (sélection multi-zones).
- **Alertes et Surveillance** :
    - Mise à jour des zones d'alerte de chalutage (exclusion des zones de dérogation) [#5533](https://github.com/MTES-MCT/monitorfish/issues/5533).
    - Amélioration du suivi des dysfonctionnements de balises et gestion des alertes associées.

### Évolutions techniques
- **Observabilité et Monitoring** : 
    - Amélioration de la remontée d'erreurs vers Sentry pour les processus backend (flows) et les hooks frontend [#5541](https://github.com/MTES-MCT/monitorfish/issues/5541), [#5539](https://github.com/MTES-MCT/monitorfish/issues/5539), [#5538](https://github.com/MTES-MCT/monitorfish/issues/5538).
- **Performance et API** : 
    - Implémentation de limites de débit (rate limiting) et de tentatives automatiques (retries) sur l'API de profondeur pour éviter les erreurs de type "Too many requests" [#5487](https://github.com/MTES-MCT/monitorfish/issues/5487).
- **Authentification et Communication** : 
    - Migration du système de chat vers un bot Tchap [#5514](https://github.com/MTES-MCT/monitorfish/issues/5514).
    - Mise en conformité de la page de connexion avec le système de design DSFR [#5548](https://github.com/MTES-MCT/monitorfish/issues/5548).
- **Tests** : Stabilisation et accélération de la suite de tests de bout en bout (E2E) avec Cypress.

### Autres changements
- **Accessibilité** : Ajout d'une page de déclaration d'accessibilité accessible depuis la page de connexion [#5553](https://github.com/MTES-MCT/monitorfish/issues/5553).
- **Documentation** : Mises à jour régulières de la documentation de l'application et des guides utilisateurs [#5527](https://github.com/MTES-MCT/monitorfish/issues/5527).
