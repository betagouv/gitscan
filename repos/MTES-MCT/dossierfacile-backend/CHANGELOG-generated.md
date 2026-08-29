## Changelog : dossierfacile-backend (30 derniers jours, au 28/08/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec l'introduction de l'autovalidation des dossiers, accompagnée d'un système d'adhésion (opt-in). Les capacités d'analyse automatique des documents ont été renforcées, tandis que l'expérience utilisateur a été fluidifiée par de nouvelles options de partage, une meilleure gestion des notifications et des corrections sur les processus de validation (DPE, avis d'imposition).

### Évolutions fonctionnelles
- **Autovalidation** : Mise en place de l'autovalidation des dossiers avec un mécanisme d'adhésion volontaire [#1283](https://github.com/MTES-MCT/dossierfacile-backend/issues/1283) [#1293](https://github.com/MTES-MCT/dossierfacile-backend/issues/1293) [#1295](https://github.com/MTES-MCT/dossierfacile-backend/issues/1295).
- **Traitement documentaire (IA)** : Amélioration de l'analyse des avis d'imposition (possibilité de télécharger un document plus récent [#1281](https://github.com/MTES-MCT/dossierfacile-backend/issues/1281)) et ajustement des règles de l'IA concernant l'année fiscale [#1306](https://github.com/MTES-MCT/dossierfacile-backend/issues/1306).
- **Expérience utilisateur et notifications** : 
    - Optimisation du timing des notifications pour les garants (envoi lors de la soumission uniquement) [#1296](https://github.com/MTES-MCT/dossierfacile-backend/issues/1296).
    - Amélioration de la récupération de mot de passe pour les propriétaires [#1300](https://github.com/MTES-MCT/dossierfacile-backend/issues/1300).
    - Ajout d'un validateur pour le format des DPE [#1299](https://github.com/MTES-MCT/dossierfacile-backend/issues/1299).
- **Partage** : Nouvelle fonctionnalité permettant de partager un dossier complété via un lien ou par email [#1301](https://github.com/MTES-MCT/dossierfacile-backend/issues/1301).
- **Backoffice** : Corrections sur la gestion des méthodes de locataires [#1298](https://github.com/MTES-MCT/dossierfacile-backend/issues/1298) et sur les liens de partage d'appartements [#1292](https://github.com/MTES-MCT/dossierfacile-backend/issues/1292).

### Évolutions techniques
- **Intelligence Artificielle** : Migration vers le workflow v2 pour le moteur de traitement documentaire (DocIA) [#1266](https://github.com/MTES-MCT/dossierfacile-backend/issues/1266).
- **Sécurité** : Correction d'une vulnérabilité potentielle concernant les webhooks propriétaires [#1290](https://github.com/MTES-MCT/dossierfacile-backend/issues/1290).
- **Tests et QA** : 
    - Création d'un utilisateur dédié pour les tests de bout en bout (E2E) dans le Backoffice [#1305](https://github.com/MTES-MCT/dossierfacile-backend/issues/1305).
    - Correction du bot de validation automatique pour la QA [#1303](https://github.com/MTES-MCT/dossierfacile-backend/issues/1303).

### Autres changements
- Validation des paramètres de configuration du système [#1291](https://github.com/MTES-MCT/dossierfacile-backend/issues/1291).
