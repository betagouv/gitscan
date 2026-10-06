## Changelog : pass-sport (30 derniers jours, au 05 octobre 2026)

### Résumé
Ce mois-ci, l'évolution majeure concerne l'intégration et le renforcement du parcours via FranceConnect, incluant de nouveaux mécanismes de relance et une meilleure gestion des erreurs. Les règles de calcul de l'éligibilité ont également été affinées pour mieux prendre en compte les situations familiales (conjoints) et les bénéficiaires de certaines aides (AAH, AEEH, boursiers).

### Évolutions fonctionnelles
- **Intégration FranceConnect** : déploiement du support de connexion FranceConnect, mise en place d'un système de relance pour les utilisateurs et amélioration de la continuité du parcours en cas d'interruption. [#627](https://github.com/betagouv/pass-sport/pull/627), [#641](https://github.com/betagouv/pass-sport/pull/641), [#597](https://github.com/betagouv/pass-sport/pull/597)
- **Affinement de l'éligibilité** : 
    - Mise à jour des règles de matching pour inclure les conjoints et améliorer la détection des bénéficiaires AAH/AEEH via le nom de famille.
    - Intégration de la situation de boursier dans les critères de calcul.
- **Communication et expérience utilisateur** :
    - Mise à jour des modèles d'emails (expéditeur, sujets et contenus) et simplification des formulations liées à l'éligibilité.
    - Ajout d'un kit de communication (flyer) pour accompagner le service.
    - Corrections d'interface, notamment sur la barre de navigation et l'accessibilité des URLs.

### Évolutions techniques
- **Fiabilité et performance** :
    - Optimisation des performances via l'ajout d'index en base de données. [#608](https://github.com/betagouv/pass-sport/pull/608)
    - Mise en place d'un limiteur de débit (*rate limiter*) sur le worker pour protéger les appels API.
    - Amélioration de la résilience de l'infrastructure Nginx (gestion des échecs d'upstream et optimisation du *keep-alive*). [#570](https://github.com/betagouv/pass-sport/pull/570)
- **Observabilité et maintenance** :
    - Amélioration du suivi des erreurs avec Sentry (intégration des *source maps* et gestion du CSP).
    - Mise à jour du plan de marquage Matomo pour un meilleur suivi analytique. [#573](https://github.com/betagouv/pass-sport/pull/573)
    - Corrections de la chaîne CI/CD et des tâches planifiées (cron) via Ansible. [#604](https://github.com/betagouv/pass-sport/pull/604)

### Autres changements
- **Nettoyage** : suppression de code et d'index inutilisés, et retrait de l'usage des codes QR.
- **Documentation** : mises à jour diverses de la documentation et du sitemap.
