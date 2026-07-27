## Changelog : AssistantMiraiLibreOffice (30 derniers jours, au 26 juillet 2026)

### Résumé
Ce mois-ci, l'extension AssistantMiraiLibreOffice a bénéficié d'améliorations significatives concernant le mécanisme de mise à jour, la gestion des erreurs et l'intégration avec les systèmes d'authentification. Des corrections ont été apportées pour une meilleure stabilité et une expérience utilisateur plus fluide, notamment lors des mises à jour et de l'accès aux fonctionnalités de l'extension.

### Évolutions fonctionnelles
- Ajout d'un bouton "Ouvrir le dossier" dans la boîte de dialogue de mise à jour bloquée, permettant d'accéder directement au dossier de l'extension pour une installation manuelle. [#7](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/7)
- Amélioration du message d'erreur affiché en cas d'échec de mise à jour, avec des instructions pour une installation manuelle.
- Correction de l'affichage du bouton "Ouvrir le dossier" qui était invisible dans certaines situations. [#12](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/12)
- Le menu contextuel fonctionne désormais correctement. [#88819ce](https://github.com/IA-Generative/AssistantMiraiLibreOffice/commit/88819ce)
- Ajout de traductions et corrections pour le menu contextuel. [#621c5c8](https://github.com/IA-Generative/AssistantMiraiLibreOffice/commit/621c5c8)

### Évolutions techniques
- Mise en place d'un mécanisme de mise à jour plus robuste avec gestion des échecs et repli sur une autre source de téléchargement. [#16](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/16)
- Installation de l'extension en cours de processus via `ExtensionManager.get()` pour une meilleure gestion et éviter les doublons. [#14](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/14)
- Amélioration de la gestion des erreurs lors de la récupération de la configuration, avec un système de cache et de failover. [#3](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/3)
- Correction d'un problème de boucle infinie lors de l'installation automatique de l'extension. [#20](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/20)
- Implémentation de l'authentification SSO Mirai via les variables d'environnement KEYCLOAK. [#2](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/2)
- Possibilité de désactiver la vérification TLS pour certaines URL via `bootstrap_insecure_urls`.
- Refactorisation de la gestion des mises à jour pour une installation "in-process" plus fiable. [#19](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/19)

### Autres changements
- Mise à jour de la documentation concernant le mécanisme de mise à jour. [#11](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/11)
- Ajout d'un guide pour les développeurs.
- Mise à jour du fichier README et du changelog.
- Amélioration des tests et correction de tests existants. [#2](https://github.com/IA-Generative/AssistantMiraiLibreOffice/commit/72d5f6d)
- Plusieurs correctifs et améliorations mineures de code.
