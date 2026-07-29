## Changelog : AssistantMiraiLibreOffice (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration du mécanisme de mise à jour de l'extension, en le rendant plus robuste et plus facile à diagnostiquer en cas de problème. Des corrections ont également été apportées pour améliorer l'intégration SSO et l'expérience utilisateur générale. Enfin, des améliorations de performance ont été apportées à la récupération de la configuration.

### Évolutions fonctionnelles
- Ajout d'un bouton "Ouvrir le dossier" dans la boîte de dialogue de mise à jour bloquée, permettant d'accéder facilement aux fichiers de l'extension pour une installation manuelle. [#7](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/7)
- Amélioration du message d'erreur lors d'une mise à jour échouée, avec des instructions pour une installation manuelle.
- Correction de l'affichage du bouton "Ouvrir le dossier" qui était invisible dans certaines situations. [#12](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/12)
- Correction de l'intégration SSO Mirai, utilisant les variables d'environnement KEYCLOAK_* pour la configuration. [#2](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/2)
- Ajout d'un menu contextuel (avec traductions et corrections). [#3](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/3)

### Évolutions techniques
- Refonte du mécanisme de mise à jour :
    - Installation "in-process" via `ExtensionManager` pour une meilleure gestion et une installation plus propre. [#19](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/19)
    - Suppression de l'ancienne version avant l'installation de la nouvelle pour éviter les conflits.
    - Amélioration de la gestion des erreurs et des échecs de téléchargement avec un mécanisme de repli (failover) sur plusieurs sources. [#16](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/16)
    - Redémarrage natif de LibreOffice après la mise à jour pour appliquer les changements. [#21](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/21)
- Amélioration de la performance de la récupération de la configuration avec un système de cache et de failover. [#3](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/3)
- Utilisation d'un singleton pour `ExtensionManager` pour garantir une instance unique. [#14](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/14)
- Correction d'une boucle potentielle lors de l'échec de l'installation automatique. [#13](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/13)

### Autres changements
- Mise à jour de la documentation pour refléter le nouveau mécanisme de mise à jour. [#11](https://github.com/IA-Generative/AssistantMiraiLibreOffice/pull/11)
- Ajout d'un guide pour les développeurs.
- Plusieurs mises à jour de version (0.0.1.0.15 -> 0.0.1.0.22) pour intégrer les corrections et améliorations.
- Ajout d'une option pour désactiver la vérification TLS par URL via `bootstrap_insecure_urls`.
