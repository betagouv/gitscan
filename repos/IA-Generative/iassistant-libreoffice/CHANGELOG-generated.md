## Changelog : iassistant-libreoffice (30 derniers jours, au 08 octobre 2026)

### Résumé
Cette période est marquée par la sortie de la version 0.3.0. Les évolutions majeures concernent l'internationalisation, permettant à l'assistant de s'adapter automatiquement à la langue de LibreOffice, ainsi qu'une refonte complète du système de mise à jour pour le rendre plus fiable et transparent. Par ailleurs, d'importants travaux de sécurisation ont été menés pour garantir que les données sensibles (identifiants, jetons) ne soient plus stockées en clair sur l'ordinateur, mais protégées par les systèmes de sécurité natifs (Windows et macOS).

### Évolutions fonctionnelles
- **Internationalisation (i18n) :**
    - L'extension détecte et suit désormais automatiquement la langue utilisée dans LibreOffice.
    - Ajout d'un réglage de la langue de l'interface dans les paramètres, applicable à l'ensemble de l'outil.
    - Traduction des dialogues de mise à jour et localisation de la palette et du moteur de l'assistant.
- **Expérience de mise à jour :**
    - Utilisation des dialogues de mise à jour natifs du système pour une meilleure intégration.
    - Mise en place d'un mécanisme de "cooldown" : si une mise à jour est refusée, elle n'est plus proposée avant 24 heures pour éviter les interruptions intempestives.
    - Simplification des messages de confirmation après une installation réussie.

### Évolutions techniques
- **Sécurité et Confidentialité :**
    - **Gestion des secrets :** Migration des jetons et identifiants vers les coffres-forts sécurisés de l'OS (Windows Keychain / macOS Keychain). Les secrets ne sont plus écrits dans les fichiers de profil.
    - **Protection des données :** Les jetons de session sont désormais stockés en mémoire vive plutôt que sur le disque.
    - **Nettoyage des logs :** Suppression des informations sensibles (corps de réponse serveur, jetons, texte du document) des fichiers de journaux pour garantir la confidentialité.
- **Architecture de mise à jour :**
    - Refonte majeure du mécanisme de mise à jour vers une architecture "pilotée par le système" (route native) pour une fiabilité accrue ([#44](https://github.com/IA-Generative/iassistant-libreoffice/issues/44), [#42](https://github.com/IA-Generative/iassistant-libreoffice/issues/42)).
    - Amélioration de la gestion des threads pour éviter les blocages lors de l'installation ([#9](https://github.com/IA-Generative/iassistant-libreoffice/issues/9)).
- **Qualité et Maintenance :**
    - **Tests d'architecture :** Introduction de tests automatisés pour valider le respect des règles d'architecture et des limites entre les couches logicielles.
    - **Refactoring :** Nettoyage massif du code mort dans le moteur, la coquille (shell) et les modules partagés. Suppression du menu contextuel Writer qui était défectueux ([#103](https://github.com/IA-Generative/iassistant-libreoffice/issues/103)).
    - **CI/CD :** Optimisation des pipelines avec l'intégration de Ruff pour le linting (support Python 3.11 et 3.12) et automatisation des releases via `release-please`.

### Autres changements
- **Documentation :** Mise à jour de la documentation utilisateur et correction d'incohérences entre la documentation et le comportement réel du code.
- **Build :** Normalisation des fichiers de description de l'extension (`description.xml`).
