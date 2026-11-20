## Changelog : infrastructure (30 derniers jours, au 19 novembre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de la sécurité et de la fiabilité de la chaîne de déploiement (CI/CD), ainsi que par la préparation d'environnements dédiés aux tests de sécurité (pentest). Les configurations DNS ont également été enrichies pour supporter de nouveaux services et outils de communication.

### Évolutions fonctionnelles
- **Gestion DNS et accès services :**
    - Ajout de nouveaux enregistrements DNS pour les services `cal`, `RDV SP bridge app` et l'entrée `claude`.
    - Configuration des accès DNS pour l'environnement de test (pentest) d' `emplois-cnav`.
    - Mise à jour des enregistrements Google Search Console pour le domaine `dora`.
    - Configuration du service de parsing entrant de Brevo dans l'environnement de démonstration.
    - Alignement des paramètres DMARC pour le domaine `reply`.

### Évolutions techniques
- **Sécurité et CI/CD :**
    - Refonte complète du workflow Terraform : séparation en plusieurs tâches distinctes (checks, plan, apply), utilisation d'environnements GitHub protégés et signature des plans pour garantir leur intégrité.
    - Renforcement de la sécurité des secrets en limitant la portée des identifiants Scaleway aux étapes strictement nécessaires.
    - Mise en place de la règle `CODEOWNERS` pour exiger systématiquement la revue des équipes DevOps.
    - Optimisation du workflow pour ne valider les plans que lors de succès des étapes précédentes.
- **Infrastructure et Monitoring :**
    - Déploiement d'une base de données et de secrets pour l'API-relay dans l'environnement de pentest d' `emplois-cnav`.
    - Intégration de la source de données des logs Cockpit pour le cluster Kubernetes d' `emplois-cnav`.
    - Automatisation du redémarrage nocturne de la VM Strongswan pour assurer la stabilité du système après les mises à jour.
- **Maintenance :**
    - Mise à jour de la version de Terraform utilisée dans la CI (passage à la version 1.17.2).

### Autres changements
- **Documentation :** Mise à jour de la documentation Terraform et des instructions relatives à l'emplacement des clés AGE pour SOPS.
- **Nettoyage :** Suppression d'enregistrements de production obsolètes (`traiteurs-engages`) et de secrets inutilisés.
