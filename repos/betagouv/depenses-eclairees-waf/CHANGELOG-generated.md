## Changelog : depenses-eclairees-waf (30 derniers jours, au 25 septembre 2026)

### Résumé
Les récentes interventions ont principalement porté sur l'ajustement des règles de sécurité (WAF) pour assurer une compatibilité fluide avec les applications protégées, notamment n8n et Metabase. L'objectif a été de supprimer les blocages injustifiés (faux positifs) tout en renforçant les outils de test et la documentation pour faciliter la maintenance du proxy.

### Évolutions fonctionnelles
- **Amélioration de l'expérience utilisateur sur Metabase** : Autorisation des téléchargements de résultats de questions sur les jeux de données.
- **Correction de connectivité sur n8n** : Rétablissement du fonctionnement des WebSockets via le transfert correct de l'en-tête `Upgrade`.

### Évolutions techniques
- **Sécurité et gestion des exceptions (ModSecurity/CRS)** :
    - Optimisation des règles pour n8n : ajout de nombreuses exceptions pour éviter les blocages sur les routes `/rest/`, les corps de workflows, les identifiants et les cookies PostHog.
    - Blocage préventif (erreur 403) du proxy de télémétrie PostHog pour n8n avant l'analyse des règles de sécurité.
    - Exemption de certaines requêtes JSON (`/api/card`) des contrôles d'injection (SQLi, RCE et PHP).
- **Optimisation et architecture** :
    - Amélioration des performances en utilisant un cache local pour les règles CRS au lieu de les charger depuis l'image Docker.
    - Refactorisation de la génération des blocs d'application via l'utilisation d'un tableau `apps`.
- **Tests et outils de développement** :
    - Mise en place d'un environnement de test Docker local pour valider la configuration Nginx générée.
    - Ajout d'un script de vérification de la limitation de débit (rate-limit) lors de la connexion.
    - Amélioration de la structure des tests (déplacement vers le répertoire `test/`) et mise à jour des images de test.
    - Ajout d'une commande dédiée pour faciliter l'ajout d'exceptions WAF.

### Autres changements
- **Documentation** : Documentation complète du projet, ajout d'instructions pour les agents et documentation de la procédure de vérification de la configuration Nginx (`nginx -T`).
