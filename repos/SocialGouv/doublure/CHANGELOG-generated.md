## Changelog : doublure (30 derniers jours, au 12 août 2026)

### Résumé
Ce mois a marqué une accélération majeure du développement, faisant passer doublure d'un prototype à un proxy de sécurité robuste. Le système est désormais capable de détecter et de remplacer de manière beaucoup plus fine les données sensibles (identités, coordonnées bancaires, adresses) tout en offrant une meilleure intégration avec les outils de développement (IDE) et les agents d'IA. La sécurité a été renforcée par une approche "fermé par défaut" et une protection accrue contre les tentatives de contournement des règles de confidentialité.

### Évolutions fonctionnelles
- **Détection avancée de données sensibles (PII) :** Amélioration significative de la reconnaissance des informations personnelles, incluant désormais les noms de personnes, les IBAN, les adresses et les formats de dates.
- **Gestion des politiques de sécurité :** Mise en place d'un mode "fermé par défaut" où seules les données explicitement autorisées sont transmises, avec une gestion granulaire par type d'entité.
- **Contrôle et personnalisation :** 
    - Possibilité de choisir les types de substituts (surrogates) via la ligne de commande.
    - Introduction de profils de configuration nommés pour adapter le comportement du proxy.
- **Support des agents IA :** Capacité de pseudonymiser les corps de messages MCP et support d'un lanceur universel pour divers agents.
- **Expérience développeur :** Développement d'une extension (VSIX) pour permettre une arbitration de la sécurité directement dans l'IDE.

### Évolutions techniques
- **Sécurisation du proxy (Forwarding) :** Correction de plusieurs vulnérabilités critiques, notamment sur le transport de données en base64, la prévention du "response smuggling" et la gestion des flux provenant de serveurs distants.
- **Durcissement de la détection (Guard/Hook) :** 
    - Portage de la garde "PreToolUse" en Go pour plus de performance et de fiabilité.
    - Amélioration de la détection des mécanismes shell (heredoc, expansion de variables, commandes exec) pour éviter les fuites via des commandes système.
- **Architecture et stockage :** 
    - Mise en place d'un coffre-fort (Vault) avec chiffrement des valeurs réelles au repos.
    - Refactorisation de la gestion de l'état pour isoler les données par projet.
    - Utilisation de sockets Unix pour l'arbitration entre les services.
- **Qualité et tests :** Ajout d'une suite de tests adverses et d'un corpus de référence ("golden corpus") pour valider l'efficacité de la pseudonymisation face à des tentatives de contournement.

### Autres changements
- **Documentation :** Migration complète de la documentation en anglais et ajout d'analyses de risques liées à la protection des données (DPO).
- **Identité du projet :** Renommage officiel du projet en "doublure".
- **Toolchain :** Introduction de `Taskfile` et `devbox` pour simplifier la gestion des environnements de développement et des commandes de build.
