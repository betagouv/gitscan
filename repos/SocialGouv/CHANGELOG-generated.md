# Synthèse d'activité : SocialGouv (du 17/04 au 29/05)

## Résumé de l'activité
L'activité récente de SocialGouv se concentre sur l'amélioration de la sécurité, la modernisation des infrastructures et l'ajout de nouvelles fonctionnalités pour faciliter l'accès à l'information et l'automatisation des tâches. Plusieurs projets ont bénéficié de migrations vers des outils plus récents (pnpm, Node.js, Python, Django) pour garantir leur pérennité et leur sécurité. Des efforts importants ont été déployés pour améliorer l'expérience utilisateur, notamment avec des corrections de bugs, des améliorations de l'interface et l'ajout de nouvelles fonctionnalités comme l'authentification à deux facteurs et la recherche sémantique. L'intégration d'IA et d'agents de codage est également en progression, avec des outils comme `git-ai-trace` et `repo-falcon` qui gagnent en maturité. Enfin, la mise à jour régulière des données légales et conventionnelles (legi-data, kali-data, code-du-travail-numerique) reste une priorité.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction d'une vulnérabilité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
- Correction de sécurité dans [archifiltre-docs](/repos/SocialGouv/archifiltre-docs).
- Renforcement de la sécurité et correction de vulnérabilités dans [smart-allow](/repos/SocialGouv/smart-allow).
- Amélioration de la sécurité avec la fermeture de vulnérabilités et l'utilisation de cosign dans [claw-code-go](/repos/SocialGouv/claw-code-go).
- Correction de l'URL de test pour le provider Proconnect dans [charon](/repos/SocialGouv/charon).

## Autres changements notables
- Migration vers pnpm dans [token-bureau](/repos/SocialGouv/token-bureau), [revu](/repos/SocialGouv/revu), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget), [domifa](/repos/SocialGouv/domifa) et [cdtn-admin](/repos/SocialGouv/cdtn-admin).
- Refonte de l'architecture de [questions-ecrites](/repos/SocialGouv/questions-ecrites) avec l'utilisation de `pg_vector` à la place de `qdrant`.
- Migration vers Node.js 20 dans [token-bureau](/repos/SocialGouv/token-bureau).
- Migration vers Python 3.14 et Django 5.2.13 dans [cdtn-admin](/repos/SocialGouv/cdtn-admin).
- Migration vers une instance interne d'Elasticsearch pour la pré-production dans [cdtn-admin](/repos/SocialGouv/cdtn-admin).
- Refonte de l'installateur de [smart-allow](/repos/SocialGouv/smart-allow).
- Ajout d'un proxy de suivi côté serveur dans [matomo-next](/repos/SocialGouv/matomo-next).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Amélioration de l'accessibilité et du processus d'agrément.
- [token-bureau](/repos/SocialGouv/token-bureau) : Corrections de bugs et migration vers pnpm.
- [srdt](/repos/SocialGouv/srdt) : Amélioration de l'expérience utilisateur et ajout de nouvelles fonctionnalités.
- [smart-allow](/repos/SocialGouv/smart-allow) : Ajout de fonctionnalités de blocage de données et refonte de l'installateur.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Refonte de l'architecture et ajout de la recherche sémantique.
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Amélioration de la gestion des contributions et migration vers Elasticsearch.
- [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi et prise en charge des tests A/B.
- [code-du-travail-numerique](/repos/SocialGouv/code-du-travail-numerique) : Amélioration du SMIC et de la recherche.
- [dashlord](/repos/SocialGouv/dashlord) : Amélioration de l'interface utilisateur et ajout de nouvelles fonctionnalités.
- [git-ai-trace](/repos/SocialGouv/git-ai-trace) : Initialisation du projet et mise en place du CI/CD.
