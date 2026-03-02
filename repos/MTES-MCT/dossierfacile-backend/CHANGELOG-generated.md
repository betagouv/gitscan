## Changelog : dossierfacile-backend (30 derniers jours)

### Résumé
Ce changelog présente les améliorations et corrections apportées au backend de DossierFacile au cours des 30 derniers jours. Les modifications incluent des améliorations de la robustesse, des corrections de bugs, des refactorings pour simplifier le code et l'ajout de fonctionnalités comme la gestion des feature flags. Plusieurs versions mineures ont été publiées pour intégrer ces changements.

### Évolutions fonctionnelles

- Ajout de la fonctionnalité de gestion des *feature flags* pour activer ou désactiver certaines fonctionnalités dynamiquement. [#1150](https://github.com/MTES-MCT/dossierfacile-backend/issues/1150)
- Amélioration du traitement des fichiers pour éviter les crashes de Tika lors de l'extraction des métadonnées. [#1145](https://github.com/MTES-MCT/dossierfacile-backend/issues/1145)
- Correction d'un bug empêchant l'envoi correct de l'application au *back office* en cas d'avertissement sur le compte. [#1130](https://github.com/MTES-MCT/dossierfacile-backend/issues/1130)
- Correction d'un problème empêchant l'ajout correct de fichiers aux documents, ce qui pouvait entraîner des vérifications de duplication incorrectes.
- Correction d'un bug dans le comptage des visites, afin de ne pas compter les visites du tenant sur son propre lien. [#1119](https://github.com/MTES-MCT/dossierfacile-backend/issues/1119)

### Évolutions techniques

- Refactorisation importante du code pour supprimer des fonctionnalités obsolètes :
    - Suppression des endpoints et du code liés aux partenaires. [#1147](https://github.com/MTES-MCT/dossierfacile-backend/issues/1147)
    - Suppression des endpoints et du code liés à FranceConnect. [#1144](https://github.com/MTES-MCT/dossierfacile-backend/issues/1144)
    - Suppression de la route et du code de régénération de token. [#1128](https://github.com/MTES-MCT/dossierfacile-backend/issues/1128)
- Amélioration de la gestion des erreurs :
    - Retour d'une erreur 404 au lieu d'une 500 lors de la recherche d'une propriété par ID. [#1134](https://github.com/MTES-MCT/dossierfacile-backend/issues/1134)
    - Ajout de logs de diagnostic pour les erreurs de verrouillage optimiste (409). [#1139](https://github.com/MTES-MCT/dossierfacile-backend/issues/1139)
    - Suppression de l'affichage des traces de pile dans les réponses de l'API. [#1138](https://github.com/MTES-MCT/dossierfacile-backend/issues/1138)
- Amélioration de la performance en activant l'exécution parallèle des tâches. [#1137](https://github.com/MTES-MCT/dossierfacile-backend/issues/1137)
- Amélioration de la logique de normalisation des URI dans les logs. [#1140](https://github.com/MTES-MCT/dossierfacile-backend/issues/1140)
- Mise à jour de la version de Spring Doc pour assurer la compatibilité. [#1125](https://github.com/MTES-MCT/dossierfacile-backend/issues/1125)
- Correction d'un problème d'encodage de l'en-tête `Content-Disposition`. [#1131](https://github.com/MTES-MCT/dossierfacile-backend/issues/1131)
- Mise à jour de l'URL du certificat Ants. [#1126](https://github.com/MTES-MCT/dossierfacile-backend/issues/1126)

### Autres changements

- Définition des IDs de templates Brevo directement dans le code au lieu des propriétés. [#1102](https://github.com/MTES-MCT/dossierfacile-backend/issues/1102)
- Publication des versions 3.4.1, 3.4.2, 3.4.3, 3.4.4, 3.4.5 et 3.4.6.
- Normalisation de l'URI dans les logs. [#1140](https://github.com/MTES-MCT/dossierfacile-backend/issues/1140)
