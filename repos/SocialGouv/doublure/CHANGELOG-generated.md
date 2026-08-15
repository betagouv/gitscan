## Changelog : doublure (30 derniers jours, au 13 août 2026)

### Résumé
Le projet a franchi une étape majeure avec la stabilisation de sa première version fonctionnelle. Doublure est désormais capable de protéger efficacement les échanges avec les IA (comme Claude) en détectant et en remplaçant automatiquement les données sensibles (noms, adresses, dates, IBAN) par des données fictives mais réalistes. Le système garantit que les informations réelles ne quittent jamais l'environnement sécurisé, tout en permettant à l'utilisateur de valider ou de refuser les décisions de protection via une interface intégrée.

### Évolutions fonctionnelles
- **Protection des données personnelles (PII) :** Amélioration de la détection et de la pseudonymisation des noms, adresses postales, dates et numéros IBAN. Les dates sont désormais "décalées" de manière cohérente pour préserver leur sens sans révéler la réalité.
- **Gestion de la confidentialité :** Mise en place d'une politique de sécurité "fermée par défaut". En cas d'incertitude, le système demande l'arbitrage de l'utilisateur sur la portée et la granularité de la protection.
- **Intégration de l'environnement de développement :** Introduction d'une extension VSCode permettant de gérer les politiques de confidentialité et l'arbitrage directement depuis l'IDE.
- **Support des protocoles distants (MCP) :** Ajout d'un proxy pour intercepter et pseudonymiser les flux de données provenant des serveurs MCP (Model Context Protocol) distants.
- **Contrôle des outils :** Capacité de bloquer l'exécution de commandes ou d'outils à haut risque avant qu'ils ne soient lancés.

### Évolutions techniques
- **Sécurisation intensive (Hardening) :** Plusieurs cycles de révision (rounds de tests adverses) ont permis de corriger de nombreuses vulnérabilités, notamment des fuites d'URL, des contournements via des commandes shell (heredoc, pipelines, exec) et des problèmes de manipulation de données encodées en base64.
- **Coffre-fort sécurisé (Vault) :** Implémentation d'un système de stockage des valeurs réelles chiffré au repos (AES-256-GCM), garantissant une restauration fidèle et injective des données.
- **Architecture de contrôle :** Développement d'un service de contrôle performant en Go, communiquant via un socket Unix, pour assurer la séparation entre l'enforcement (protection) et l'interface de contrôle.
- **Validation et tests :** Mise en place de suites de tests adverses, d'un "golden corpus" pour la validation des modèles, et d'un dispositif de test de l'égress réseau pour prouver l'étanchéité du système.
- **Optimisation du moteur de détection :** Amélioration de la précision de la détection par l'intégration de modèles de type NER (Named Entity Recognition) et de règles de forme (shape rules).

### Autres changements
- **Identité du projet :** Renommage officiel du projet en "doublure".
- **Documentation :** Mise à jour complète de la documentation (README, guides de transfert) et migration de la documentation technique vers l'anglais.
- **Standardisation :** Adoption de `Taskfile` pour la gestion des commandes et de `devbox` pour la gestion de la chaîne d'outils.
