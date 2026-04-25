# Synthèse d'activité : demarche-numerique (du 27/03 au 03/04)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) avec de nouvelles fonctionnalités pour les utilisateurs et les administrateurs. Les utilisateurs peuvent désormais joindre des fichiers dans des formats plus variés et bénéficier d'une meilleure gestion de leurs dossiers. Les administrateurs ont plus de contrôle sur la présentation des procédures. Parallèlement, des efforts importants ont été déployés pour renforcer la sécurité et moderniser l'infrastructure, notamment avec la migration de composants et l'amélioration de la gestion des images Docker pour [ds_proxy](/repos/demarche-numerique/ds_proxy).

## Sécurité
- Renforcement de la sécurité de l'authentification FranceConnect et correction de vulnérabilités liées aux URL et à l'injection de code dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- Migration de composants HAML vers ERB dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Refonte du processus de construction des images Docker dans [ds_proxy](/repos/demarche-numerique/ds_proxy) pour simplifier la création d'images.
- Utilisation de WeasyPrint pour la génération d'attestations de dépôt en PDF dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Ajout de fonctionnalités pour la gestion des pièces justificatives, l'administration des procédures et l'amélioration de l'expérience utilisateur.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Simplification de la construction des images Docker et amélioration de l'information sur les versions.
