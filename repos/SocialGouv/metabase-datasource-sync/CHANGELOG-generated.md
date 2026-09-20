## Changelog : metabase-datasource-sync (30 derniers jours, au 14/09/2026)

### Résumé
Le projet franchit une étape majeure avec le lancement de sa fonctionnalité principale : la synchronisation automatique des accès aux bases de données. Cet outil permet de garantir que les outils de reporting (Metabase) restent connectés et opérationnels, même lors du renouvellement automatique des mots de passe et des clés de sécurité.

### Évolutions fonctionnelles
- Mise en œuvre du moteur de réconciliation des sources de données, permettant la synchronisation automatique des connexions Metabase.

### Évolutions techniques
- **Fiabilité et exploitation :**
    - Ajout d'une sonde de santé (*liveness probe*) via l'option `--liveness` pour améliorer le monitoring dans les environnements Kubernetes.
    - Correction d'un bug de lecture des secrets Kubernetes (gestion des liens symboliques) pour assurer la stabilité en cluster.
- **Qualité et CI/CD :**
    - Mise en place de tests d'acceptation réalisés sur des instances réelles de Metabase et PostgreSQL.
    - Initialisation et activation des workflows d'intégration continue (CI).
    - Stabilisation du processus de construction (*build*) par l'alignement strict des versions du projet (`Cargo.toml` et `Cargo.lock`).

### Autres changements
- Mise à jour de la documentation (README) pour supprimer les liens internes et préparer le dépôt à une publication publique.
