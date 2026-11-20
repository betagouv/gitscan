## Changelog : GatewAI (30 derniers jours, au 20 novembre 2026)

### Résumé
GatewAI a franchi une étape importante avec l'introduction d'un adaptateur capable de transformer des fichiers (comme des images) en requêtes de chat compatibles OpenAI, facilitant l'usage des modèles de vision. Cette période a également été marquée par des optimisations de performance sur le suivi de consommation et une mise à jour de l'infrastructure de base pour renforcer la sécurité.

### Évolutions fonctionnelles
- **Nouvel adaptateur d'entrée générique (`multipart_to_chat`)** : permet de convertir automatiquement des téléchargements de fichiers (multipart) en requêtes de chat au format OpenAI (synchrone et asynchrone).
- **Contrôle de l'ordre des messages** : ajout de l'option `prompt_last` permettant de placer le texte après le fichier, une fonctionnalité essentielle pour le bon fonctionnement de certains modèles d'OCR et de vision.

### Évolutions techniques
- **Optimisation des performances** : amélioration du pipeline de suivi de la consommation (usage) via une réduction des lectures Redis et une gestion optimisée des clés de budget.
- **Correction de la gestion des modèles** : l'identifiant du modèle de backend (`backend_model`) est désormais correctement appliqué lors de l'utilisation de l'adaptateur en mode asynchrone [#232](https://github.com/IA-Generative/GatewAI/pull/232).
- **Amélioration de la télémétrie** : correction du chemin de l'exportateur OTLP pour cibler correctement les endpoints `/v1/*` [#204](https://github.com/IA-Generative/GatewAI/pull/204).
- **Mise à jour de l'infrastructure** : passage à Go 1.27 et utilisation d'images distroless Debian 13 pour améliorer la sécurité et la légèreté des conteneurs.

### Autres changements
- **Documentation** : documentation complète du nouvel adaptateur d'entrée et intégration dans les charts Helm [#230](https://github.com/IA-Generative/GatewAI/pull/230) ; traduction de la page d'accueil en anglais.
- **Nettoyage** : suppression de la documentation obsolète (`ARCHITECTURE.md`) et correction des liens dans les guides d'exploitation (runbooks).
- **Identité et conformité** : migration des références de l'organisation `Qatr-io` vers `IA-Generative` et mise à jour des droits de licence [#203](https://github.com/IA-Generative/GatewAI/pull/203).
- **Docker** : ajout de labels OCI pour améliorer la traçabilité des images sur GHCR.
