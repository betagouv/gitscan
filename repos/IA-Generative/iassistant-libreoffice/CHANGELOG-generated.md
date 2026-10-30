## Changelog : iassistant-libreoffice (30 derniers jours, au 08/10/2026)

### Résumé
Cette période est marquée par la publication de la version 0.3.0. Les évolutions majeures concernent l'internationalisation, permettant à l'assistant de s'adapter automatiquement à la langue de LibreOffice, ainsi qu'un renforcement significatif de la sécurité et de la confidentialité des données (meilleure gestion des secrets et nettoyage des journaux de bord).

### Évolutions fonctionnelles
- **Internationalisation (i18n) :**
    - L'extension s'adapte désormais automatiquement à la langue configurée dans LibreOffice. [#41](https://github.com/IA-Generative/iassistant-libreoffice/pull/41)
    - Traduction des dialogues de mise à jour et des suggestions/explications de l'interface.
    - Les transformations de texte respectent désormais la langue du document en cours.
    - Amélioration de l'affichage et de l'alignement pour les langues comme le chinois.
- **Paramètres :** Possibilité de choisir manuellement la langue de l'interface dans les réglages.

### Évolutions techniques
- **Sécurité et Confidentialité :**
    - Migration des secrets (jetons, identifiants) vers les coffres-forts natifs (Windows et macOS) et stockage en mémoire pour limiter les traces sur le disque.
    - Protection des données sensibles : suppression des jetons, des réponses serveurs et du contenu des documents des fichiers de journaux (logs).
    - Retrait des clés de télémétrie codées en dur.
- **Gestion du stockage et de l'installation :**
    - Centralisation des fichiers de l'extension, des caches et des configurations dans un nouveau répertoire dédié (`mirai/`).
    - Amélioration du processus de désinstallation pour garantir un effacement complet des données. [#49](https://github.com/IA-Generative/iassistant-libreoffice/pull/49)
- **Architecture et Qualité logicielle :**
    - Introduction de tests de règles d'architecture pour garantir l'intégrité des couches logicielles et des commandes.
    - Refactoring majeur pour supprimer le code mort et les menus contextuels obsolètes (notamment dans Writer).
    - Optimisation des processus de démarrage via une meilleure gestion des threads.
- **CI/CD :**
    - Mise à jour des pipelines de tests pour supporter Python 3.11 et 3.12.
    - Automatisation de la gestion des versions et du changelog.

### Autres changements
- Mise à jour de la documentation utilisateur et correction de certaines incohérences techniques.
