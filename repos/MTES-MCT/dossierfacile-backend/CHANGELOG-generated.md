## Changelog : dossierfacile-backend (30 derniers jours)

### Résumé
Ce changelog résume les évolutions récentes du backend de DossierFacile.fr. Les mises à jour incluent des améliorations de la sécurité, des corrections de bugs, des optimisations de performance et des refactorings importants pour simplifier et clarifier le code. Des nouvelles fonctionnalités ont également été ajoutées, notamment la gestion des feature flags et l'accès restreint à certaines fonctionnalités pour les administrateurs.

### Évolutions fonctionnelles
- Les administrateurs peuvent désormais accéder et visualiser les fichiers bruts. [#1156](https://github.com/MTES-MCT/dossierfacile-backend/issues/1156)
- Ajout d'un nouvel endpoint pour récupérer les documents via un lien spécifique : `/api/application/links/{linkToken}/document/{documentName}` et restriction de l'accès à l'endpoint `/api/document/resource/{uuid}` à une authentification.
- Gestion améliorée des liens de documents pour les partenaires.
- Correction d'un bug qui empêchait l'affichage correct des URL de prévisualisation.
- Ajout de la fonctionnalité de feature flags, permettant d'activer ou de désactiver des fonctionnalités sans redéploiement. [#1150](https://github.com/MTES-MCT/dossierfacile-backend/issues/1150)
- Amélioration de la gestion des visites de liens par les tenants (éviter le comptage des visites par le tenant lui-même). [#1119](https://github.com/MTES-MCT/dossierfacile-backend/issues/1119)

### Évolutions techniques
- Refactorings importants pour supprimer du code obsolète et simplifier l'architecture, notamment concernant les endpoints liés aux partenaires, FranceConnect et la régénération de tokens. [#1147](https://github.com/MTES-MCT/dossierfacile-backend/issues/1147), [#1145](https://github.com/MTES-MCT/dossierfacile-backend/issues/1145), [#1144](https://github.com/MTES-MCT/dossierfacile-backend/issues/1144), [#1128](https://github.com/MTES-MCT/dossierfacile-backend/issues/1128), [#1129](https://github.com/MTES-MCT/dossierfacile-backend/issues/1129)
- Amélioration de la gestion des erreurs et ajout de logs de diagnostic pour faciliter le débogage.
- Optimisation de l'exécution des tâches planifiées pour permettre un traitement parallèle. [#1137](https://github.com/MTES-MCT/dossierfacile-backend/issues/1137)
- Amélioration de la robustesse de la gestion des erreurs Optimistic Locking. [#1139](https://github.com/MTES-MCT/dossierfacile-backend/issues/1139)
- Correction d'un problème de crash de Tika lors de l'extraction de métadonnées. [#1125](https://github.com/MTES-MCT/dossierfacile-backend/issues/1125)
- Mise à jour de la version de spring-doc pour assurer la compatibilité.
- Amélioration de la gestion des en-têtes `Content-Disposition` pour éviter les erreurs d'encodage. [#1100](https://github.com/MTES-MCT/dossierfacile-backend/issues/1100)
- Amélioration de la journalisation des adresses IP des clients en utilisant l'en-tête `X-Forwarded-For`. [#1165](https://github.com/MTES-MCT/dossierfacile-backend/issues/1165), [#1164](https://github.com/MTES-MCT/dossierfacile-backend/issues/1164)

### Autres changements
- Ajout de tests unitaires et d'intégration pour le mapper des tenants.
- Mise à jour des IDs de templates Brevo en dur dans le code. [#1102](https://github.com/MTES-MCT/dossierfacile-backend/issues/1102)
- Suppression de la configuration par email des clients partenaires. [#1143](https://github.com/MTES-MCT/dossierfacile-backend/issues/1143)
- Plusieurs corrections de bugs et améliorations mineures.
- Mises à jour de version (v3.4.6, v3.4.8, v3.4.9, v3.4.10, v3.4.11, v3.4.12).
