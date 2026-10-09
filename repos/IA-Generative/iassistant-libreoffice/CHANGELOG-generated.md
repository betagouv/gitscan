## Changelog : iassistant-libreoffice (30 derniers jours, au 08/10/2026)

### Résumé
Cette période a été marquée par la sortie de la version 0.3.0, apportant une dimension internationale au projet grâce à la traduction de l'interface. La sécurité a été considérablement renforcée pour mieux protéger les données sensibles, et le système de mise à jour a été entièrement repensé pour être plus fiable, plus stable et moins intrusif pour l'utilisateur.

### Évolutions fonctionnelles
- **Internationalisation (i18n) :** L'extension s'adapte désormais automatiquement à la langue de LibreOffice. Les dialogues de mise à jour, la palette d'outils et le moteur sont traduits, et les suggestions textuelles respectent la langue du document ou de l'interface. [#41](https://github.com/IA-Generative/iassistant-libreoffice/pull/41)
- **Expérience de mise à jour :** Le processus de mise à jour est plus fluide. En cas de refus de l'utilisateur, un délai de "cooldown" de 24 heures est appliqué avant de proposer à nouveau la mise à jour, évitant ainsi les sollicitations répétitives.

### Évolutions techniques
- **Sécurité et confidentialité :** Les informations sensibles (secrets, jetons) sont désormais stockées dans les coffres-forts natifs des systèmes d'exploitation (Windows et macOS) plutôt que dans des fichiers de profil. Les journaux (logs) ont été nettoyés pour ne plus contenir de jetons d'authentification ni de contenu de documents.
- **Fiabilité des mises à jour :** Refonte complète du mécanisme de mise à jour pour garantir une installation stable, incluant une meilleure gestion des threads, une détection native de l'installation et l'ajout de télémétrie pour faciliter le diagnostic technique. [#9](https://github.com/IA-Generative/iassistant-libreoffice/issues/9)
- **Qualité logicielle et CI/CD :** 
    - Introduction de tests de règles d'architecture pour garantir la structure du code.
    - Amélioration de la chaîne de tests automatisés (CI) avec un support étendu pour Python 3.11 et 3.12 et l'utilisation de Ruff pour le linting.
- **Refactoring :** Nettoyage important du code mort dans le moteur (engine) et l'interface (shell), et suppression du menu contextuel Writer qui était défectueux.

### Autres changements
- **Documentation :** Mise à jour de la documentation utilisateur et du fichier README.
- **Organisation du stockage :** Regroupement des fichiers de configuration, des caches et des identifiants dans un répertoire dédié (`mirai/`) pour une meilleure gestion de l'empreinte d'installation.
