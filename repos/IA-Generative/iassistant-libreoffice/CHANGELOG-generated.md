## Changelog : iassistant-libreoffice (30 derniers jours, au 2026-10-08)

### Résumé
Cette période est marquée par la sortie de la version 0.3.0. Les évolutions majeures concernent l'internationalisation complète de l'outil, une refonte profonde du système de mise à jour pour plus de fiabilité, et un renforcement significatif de la sécurité et de la confidentialité des données utilisateur (protection des secrets et nettoyage des journaux).

### Évolutions fonctionnelles
- **Internationalisation (i18n) :** L'extension s'adapte désormais automatiquement à la langue de LibreOffice. Les dialogues, la palette d'outils et le moteur sont localisés, et l'utilisateur peut configurer sa langue préférée directement dans les paramètres.
- **Gestion des mises à jour :** Le processus de mise à jour est devenu plus intelligent et moins intrusif, incluant notamment un délai de 24h avant de proposer à nouveau une mise à jour si l'utilisateur l'a refusée.
- **Désinstallation :** Amélioration du processus de suppression de l'extension pour garantir un effacement complet des données.

### Évolutions techniques
- **Sécurité et Confidentialité :**
    - Migration des secrets (jetons, clés) vers les coffres-forts natifs du système d'exploitation (Windows et macOS).
    - Protection de la vie privée : suppression des données sensibles (contenu des documents, jetons, réponses serveur) des fichiers de journaux (logs).
    - Les jetons de session sont désormais conservés uniquement en mémoire pour limiter les traces sur le disque.
- **Architecture et Système :**
    - Refonte complète du moteur de mise à jour pour une meilleure gestion des processus en arrière-plan et de l'état de l'installation ([#5](https://github.com/IA-Generative/iassistant-libreoffice/issues/5), [#9](https://github.com/IA-Generative/iassistant-libreoffice/issues/9)).
    - Nettoyage technique : suppression du menu contextuel Writer défectueux et du code mort.
    - Introduction de tests automatisés pour valider les règles d'architecture (respect des couches et des limites du système).
- **Stockage et CI/CD :**
    - Centralisation des fichiers de configuration, des caches et des journaux dans un nouveau répertoire structuré `mirai/`.
    - Optimisation de la CI avec des tests de linting et de compatibilité sur Python 3.11 et 3.12.

### Autres changements
- Mise à jour de la documentation utilisateur et des liens d'aide.
- Nettoyage des fichiers de build et des commentaires obsolètes.
