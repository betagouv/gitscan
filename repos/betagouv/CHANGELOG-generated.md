# Synthèse d'activité : betagouv (du 23 mai au 03 juin 2026)

## Résumé de l'activité
L'organisation betagouv a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs fronts. Un effort important a été consacré à la sécurité, avec des mises à jour de dépendances et des corrections de vulnérabilités dans plusieurs dépôts ([mon-suivi-justice](https://github.com/betagouv/mon-suivi-justice), [omniauth-microsoft_graph](https://github.com/betagouv/omniauth-microsoft_graph)). De nombreuses améliorations fonctionnelles ont été déployées, notamment sur [zacharie](https://github.com/betagouv/zacharie) avec de nouvelles fonctionnalités de gestion des données et des utilisateurs, et sur [jeveuxaider-front](https://github.com/betagouv/jeveuxaider-front) avec une refonte de l'interface de partage de missions. Plusieurs projets ont bénéficié de refactorisations techniques importantes, comme [test-sme](https://github.com/betagouv/test-sme) et [pitchou](https://github.com/betagouv/pitchou), visant à améliorer la maintenabilité et la performance. L'intégration de nouvelles sources de données et l'amélioration des processus de synchronisation ont également été des thèmes récurrents, notamment dans [mle-back](https://github.com/betagouv/mle-back) et [infomedicament-dataeng](https://github.com/betagouv/infomedicament-dataeng).

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :

- Correction d'une vulnérabilité XSS potentielle dans [seves](https://github.com/betagouv/seves).
- Mise à jour de dépendances pour corriger des vulnérabilités dans [recoco-sync](https://github.com/betagouv/recoco-sync), [mon-suivi-justice](https://github.com/betagouv/mon-suivi-justice) et [infomedicament-html-parser](https://github.com/betagouv/infomedicament-html-parser).
- Renforcement de la sécurité de l'authentification dans [oauth2-proxy-buildpack](https://github.com/betagouv/oauth2-proxy-buildpack).

## Autres changements notables
Plusieurs projets ont subi des refactorisations techniques majeures :

- Migration vers TypeScript dans [pitchou](https://github.com/betagouv/pitchou) pour une meilleure maintenabilité.
- Refonte de l'architecture de [maestro](https://github.com/betagouv/maestro) avec l'ajout d'un service OIDC local.
- Passage à Next.js 16 dans [jeveuxaider-front](https://github.com/betagouv/jeveuxaider-front).
- Refactorisation de la gestion des workflows dans [mission-transition-ecologique-back](https://github.com/betagouv/mission-transition-ecologique-back).
- Migration vers SQLAlchemy dans [infomedicament-dataeng](https://github.com/betagouv/infomedicament-dataeng).

## Dépôts les plus actifs
- [zacharie](https://github.com/betagouv/zacharie) : Ajout de nouvelles fonctionnalités de gestion des données et des utilisateurs.
- [sylvasan](https://github.com/betagouv/sylvasan) : Amélioration de l'expérience utilisateur avec l'ajout de l'authentification DSF et d'un champ carte.
- [test-sme](https://github.com/betagouv/test-sme) : Refonte de l'interface utilisateur et correction de bugs.
- [pitchou](https://github.com/betagouv/pitchou) : Refonte complète de l'application et amélioration de la gestion des administrateurs.
- [maestro](https://github.com/betagouv/maestro) : Ajout de nouvelles fonctionnalités pour la gestion des prélèvements et des laboratoires.
- [infomedicament](https://github.com/betagouv/infomedicament) : Amélioration de la recherche sémantique et optimisation des performances.
- [mle-back](https://github.com/betagouv/mle-back) : Amélioration de la synchronisation des données et optimisation des requêtes.
- [jeveuxaider-front](https://github.com/betagouv/jeveuxaider-front) : Refonte de l'interface de partage de missions.
