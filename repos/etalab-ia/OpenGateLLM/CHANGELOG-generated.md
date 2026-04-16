## Changelog : OpenGateLLM (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes d'architecture interne, de sécurité et de correction de bugs. Les efforts se sont concentrés sur la refactorisation du code pour une meilleure maintenabilité et l'ajout d'outils de sécurité pour identifier les vulnérabilités potentielles. Des corrections ont également été apportées à l'interface utilisateur et à certaines fonctionnalités pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- Correction du code de langue par défaut pour la transcription audio, passant de "english" à "en" [#807](https://github.com/etalab-ia/OpenGateLLM/issues/807).
- Amélioration de l'interface utilisateur du "playground" : correction de l'affichage des valeurs non sélectionnées dans les formulaires de provider, router et utilisateur [#802](https://github.com/etalab-ia/OpenGateLLM/issues/802).
- Support des signatures legacy pour l'utilisation des "impacts" [#791](https://github.com/etalab-ia/OpenGateLLM/issues/791).
- Correction d'un bug empêchant le filtrage correct des collections via l'API GET /v1/collections [#789](https://github.com/etalab-ia/OpenGateLLM/issues/789).
- Correction d'un appel manquant à `get_document_chunk` dans la gestion des chunks [#782](https://github.com/etalab-ia/OpenGateLLM/issues/782).

### Évolutions techniques
- Refactorisation importante de `BaseModelProvider` pour nettoyer l'architecture du projet [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796).
- Refactorisation de l'endpoint `/v1/admin/roles` vers une architecture plus propre [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808) et [#801](https://github.com/etalab-ia/OpenGateLLM/issues/801).
- Séparation de la clé de chiffrement des clés API du mot de passe maître [#779](https://github.com/etalab-ia/OpenGateLLM/issues/779).
- Ajout de l'outil Trivy pour la sécurité de la chaîne d'approvisionnement (supply chain) [#793](https://github.com/etalab-ia/OpenGateLLM/issues/793).
- Ajout de règles Semgrep pour améliorer la sécurité du code [#794](https://github.com/etalab-ia/OpenGateLLM/issues/794) et [#797](https://github.com/etalab-ia/OpenGateLLM/issues/797).
- Nettoyage des schémas de modèles (provider et routers) [#783](https://github.com/etalab-ia/OpenGateLLM/issues/783).
- Amélioration de la configuration des tests d'intégration [#780](https://github.com/etalab-ia/OpenGateLLM/issues/780).

### Autres changements
- Mise à jour de la documentation générée et des versions de publication [#795](https://github.com/etalab-ia/OpenGateLLM/issues/795).
- Début de l'implémentation d'un workflow Semgrep [#51bde257](https://github.com/etalab-ia/OpenGateLLM/commit/51bde257).
- Refactorisation initiale de l'administration (bootstrap) [#799](https://github.com/etalab-ia/OpenGateLLM/issues/799).
