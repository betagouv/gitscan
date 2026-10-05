## Changelog : iassistant-libreoffice (30 derniers jours, au 02 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure en renforçant considérablement la sécurité des données et la fiabilité du processus de mise à jour. L'accent a été mis sur la protection des informations sensibles (secrets) et sur une gestion plus intelligente et "native" des mises à jour de l'extension, tout en garantissant un nettoyage complet lors de la désinstallation.

### Évolutions fonctionnelles
- **Gestion des mises à jour :** Introduction d'un nouveau flux de mise à jour "native" piloté. En cas de refus de l'utilisateur, un délai de 24 heures (cooldown) est appliqué avant toute nouvelle proposition pour éviter les sollicitations répétitives [#9, #5].
- **Désinstallation propre :** Amélioration du processus de désinstallation qui permet désormais un effacement complet des données et des traces de l'application sur le système [#49].
- **Expérience utilisateur :** Simplification des messages de fermeture après une installation pour une interface plus fluide.

### Évolutions techniques
- **Sécurité et Confidentialité :** 
    - Sécurisation massive des données sensibles : les secrets ne sont plus stockés dans les fichiers de profil mais utilisent les coffres-forts natifs des systèmes d'exploitation (Windows et macOS) ou sont conservés uniquement en mémoire.
    - Protection de la vie privée : les journaux (logs) ont été nettoyés pour ne plus contenir de jetons d'accès, de réponses serveur ou de contenu textuel des documents traités.
- **Moteur de mise à jour :** 
    - Refonte profonde de l'architecture de mise à jour pour améliorer la fiabilité (gestion des threads, détection via le registre système et réconciliation des états) [#9].
    - Ajout d'une télémétrie détaillée pour assurer l'observabilité du cycle de vie des mises à jour [#9, #5].
- **Stockage et Configuration :** 
    - Centralisation des fichiers, caches et journaux dans un nouveau répertoire dédié `mirai/`.
    - Mise en place d'une lecture de configuration par couches pour une meilleure gestion des paramètres par défaut et des réglages utilisateurs.
- **Infrastructure et Qualité :** 
    - Automatisation complète des tests unitaires, d'intégration et des builds de vérification (smoke builds) dans le pipeline CI/CD à chaque modification.

### Autres changements
- **Documentation :** Mise à jour de la documentation utilisateur, du README et des spécifications techniques pour refléter les nouveaux comportements.
- **Maintenance :** Nettoyage du code (suppression de constantes magiques) et refactorisation des routes de mise à jour.
