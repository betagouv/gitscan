## Changelog : device-management (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, le projet device-management a bénéficié d'une attention particulière à la sécurité, avec une série de correctifs suite à un audit. Des améliorations ont également été apportées au déploiement, à la gestion des secrets et à l'exposition de l'API, notamment pour faciliter l'intégration avec des outils externes et améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- L'API `/catalog/api/plugins` expose désormais l'ID du plugin au lieu de son slug, facilitant l'intégration avec les clients. [#4cf65d4](https://github.com/IA-Generative/device-management/commit/4cf65d4)
- Amélioration de la génération des fichiers de mise à jour (gupdate XML et Mozilla JSON) pour supporter plusieurs cibles et utiliser des alias. [#cb68812](https://github.com/IA-Generative/device-management/commit/cb68812)
- Possibilité de configurer l'API via des variables d'environnement pour des URLs spécifiques (API_BASE, RELAY_ASSISTANT_BASE_URL, etc.). [#f49adde](https://github.com/IA-Generative/device-management/commit/f49adde)
- Le catalogue accepte maintenant un token de service pour la configuration. [#d259e01](https://github.com/IA-Generative/device-management/commit/d259e01)

### Évolutions techniques
- **Sécurité :** Correction de plusieurs vulnérabilités identifiées lors d'un audit de sécurité (CT-1, CT-7, CT-9, CT-12, IMM-1..8). [#e6a9cb2](https://github.com/IA-Generative/device-management/commit/e6a9cb2), [#c66be0d](https://github.com/IA-Generative/device-management/commit/c66be0d), [#adb4658](https://github.com/IA-Generative/device-management/commit/adb4658)
- **Déploiement :**  Amélioration du runbook de déploiement pour Scaleway et DGX. [#945aeeb](https://github.com/IA-Generative/device-management/commit/945aeeb)
- **Gestion des secrets :** Normalisation de la gestion des secrets Kubernetes, en retirant les secrets du dépôt et en utilisant des overlays par environnement. [#74941bf](https://github.com/IA-Generative/device-management/commit/74941bf), [#ed793b7](https://github.com/IA-Generative/device-management/commit/ed793b7), [#2b071c0](https://github.com/IA-Generative/device-management/commit/2b071c0)
- **Base de données :** Ajout des champs `extension_id` et `gecko_id` à la base de données pour lier les versions aux artefacts. [#3c8edb9](https://github.com/IA-Generative/device-management/commit/3c8edb9)
- Augmentation de `proxy-buffer-size` dans la configuration Nginx pour gérer les gros cookies. [#8e180b8](https://github.com/IA-Generative/device-management/commit/8e180b8)
- Correction du routage du redirect OIDC pour l'administration. [#221c849](https://github.com/IA-Generative/device-management/commit/221c849)
- Amélioration de la récupération du JWKS via l'URL interne. [#b85f689](https://github.com/IA-Generative/device-management/commit/b85f689)

### Autres changements
- Documentation : Ajout d'une section "Comment fonctionnent les mises à jour" au README. [#311c293](https://github.com/IA-Generative/device-management/commit/311c293)
- Documentation : Restructuration de la documentation par audience et suppression des artefacts internes. [#000b4fa](https://github.com/IA-Generative/device-management/commit/000b4fa)
- Documentation : Regroupement des documents ADR et de référence dans un dossier dédié. [#30754be](https://github.com/IA-Generative/device-management/commit/30754be)
- Note de sécurité ajoutée au dépôt public. [#745eed3](https://github.com/IA-Generative/device-management/commit/745eed3)
- Rapport d'audit de sécurité anonymisé ajouté. [#bb8b8e4](https://github.com/IA-Generative/device-management/commit/bb8b8e4)
- Nettoyage du code. [#b9408f3](https://github.com/IA-Generative/device-management/commit/b9408f3)
- Suppression de code mort. [#cf95cf6](https://github.com/IA-Generative/device-management/commit/cf95cf6)
