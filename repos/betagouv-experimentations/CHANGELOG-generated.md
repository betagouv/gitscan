# Synthèse d'activité : betagouv-experimentations (du 13/05 au 26/05)

## Résumé de l'activité
L'activité de l'organisation est marquée par une phase intense de prototypage et de mise en place d'infrastructures. De nombreux nouveaux projets voient le jour, utilisant une stack technologique standardisée (Next.js, React, PostgreSQL, Drizzle ORM) et le Design System Français (DSFR) pour faciliter la création rapide de services destinés à l'administration.

L'accent est mis sur l'automatisation du déploiement via Coolify et l'intégration de l'intelligence artificielle pour assister le développement. Des outils concrets émergent, comme une application de suivi de contacts pour l'équipe ASN ([crm-asn](/repos/betagouv-experimentations/crm-asn)) et une application de gestion de tâches ([repo-test](/repos/betagouv-experimentations/repo-test)).

## Sécurité
- Correction d'une vulnérabilité d'injection SQL de haute sévérité via la mise à jour de `drizzle-orm` et `drizzle-kit` dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité dans [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Amélioration de l'authentification dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) via l'appartenance à une organisation GitHub.

## Autres changements notables
- **Automatisation et infrastructure** : Intégration de l'auto-provisionnement Coolify et de workflows CI/CD pour accélérer la mise en production ([template-proto](/repos/betagouv-experimentations/template-proto), [test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2)).
- **Optimisation de l'IA** : Amélioration de l'usage de l'IA via l'invocation de compétences Claude et l'ajout d'étapes de cadrage dans [template-proto](/repos/betagouv-experimentations/template-proto).
- **Gestion des données** : Automatisation des migrations de base de données au démarrage des conteneurs dans [template-proto](/repos/betagouv-experimentations/template-proto).
- **Outils de monitoring** : Développement d'un proxy pour la récupération et l'analyse des logs Coolify ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'un outil de suivi de contacts et configuration de l'infrastructure.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Ajout de fonctionnalités de récupération de logs et de gestion d'erreurs.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Optimisation des processus de déploiement et d'utilisation de l'IA.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Mise en place d'une application de gestion de tâches complète avec persistance de données.
