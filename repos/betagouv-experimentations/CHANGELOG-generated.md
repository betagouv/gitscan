# Synthèse d'activité : betagouv-experimentations (du 13/05 au 26/05)

## Résumé de l'activité
L'activité de l'organisation est marquée par une phase intense d'initialisation de nouveaux prototypes et de mise en place d'infrastructures de déploiement automatisées. La majorité des nouveaux projets adoptent un socle technologique standardisé (Next.js, React, PostgreSQL, Drizzle ORM) et s'appuient sur l'outil Coolify pour faciliter le déploiement continu et la gestion des ressources.

Parallèlement, des outils concrets voient le jour, comme une application de suivi de contacts pour l'équipe ASN ([crm-asn](/repos/betagouv-experimentations/crm-asn)) ou une application de gestion de tâches ([repo-test](/repos/betagouv-experimentations/repo-test)). L'intégration de l'intelligence artificielle dans les flux de développement est également une tendance forte, notamment via l'utilisation de capacités Claude pour assister la création de services web et l'automatisation de certaines étapes de build.

## Sécurité
- Correction d'une vulnérabilité critique d'injection SQL via la mise à jour des outils d'ORM dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité dans [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Mise en place d'un système d'authentification basé sur l'appartenance à une organisation GitHub pour [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Autres changements notables
- **Infrastructure et Déploiement** : Généralisation de l'utilisation de Coolify pour l'auto-provisionnement et le déploiement CI/CD sur l'ensemble des nouveaux projets ([test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2), [test-jb1](/repos/betagouv-experimentations/test-jb1), [test-benoit](/repos/betagouv-experimentations/test-benoit), [simulation-doctorat](/repos/betagouv-experimentations/simulation-doctorat), [eval-metier-rag](/repos/betagouv-experimentations/eval-metier-rag), [26052026](/repos/betagouv-experimentations/26052026)).
- **Expérimentation IA** : Intégration de compétences liées à l'IA (skills Claude) dans les processus de build et de développement pour [template-proto](/repos/betagouv-experimentations/template-proto) et [repo-test](/repos/betagouv-experimentations/repo-test).
- **Observabilité** : Développement d'un proxy dédié à la gestion et à la récupération des logs pour améliorer le suivi des applications déployées via [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'un outil de suivi des contacts et des interactions pour l'équipe ASN.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Création d'un proxy pour la récupération et l'analyse des logs d'exécution.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Évolution du template de prototypage avec automatisation et intégration d'IA.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Mise en place d'une application de gestion de tâches complète avec persistance de données.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Maintenance de sécurité et ajustements de l'interface utilisateur.
