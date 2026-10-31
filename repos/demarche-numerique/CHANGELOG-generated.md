# Synthèse d'activité : demarche-numerique (du 13/10 au 20/10)

## Résumé de l'activité
L'activité de l'organisation a été marquée par des avancées significatives dans l'automatisation de la lecture de documents et la résilience des services. [la_taupe](/repos/demarche-numerique/la_taupe) a considérablement renforcé sa capacité d'extraction de données bancaires (RIB) grâce à un nouveau moteur d'OCR et l'introduction du traitement par lots. 

Parallèlement, [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) se concentre sur l'amélioration de l'expérience utilisateur et la continuité de service, notamment avec l'introduction d'un mode dégradé en cas d'indisponibilité des API. Enfin, l'écosystème s'étend avec le lancement de nouveaux projets dédiés à la documentation et à la collaboration communautaire.

## Sécurité
- Renforcement de la sécurité des comptes "Super Admin" via l'introduction de l'authentification à usage unique (OTP) et du verrouillage automatique dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Infrastructure et performance :** Migration vers Sidekiq 8 pour la gestion des tâches de fond et implémentation d'un sandboxing pour le traitement sécurisé des images dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Évolutions du stockage :** Extension des capacités de [ds_proxy](/repos/demarche-numerique/ds_proxy) avec la prise en charge de S3 et Swift.
- **Nouveaux projets structurants :** Initialisation des dépôts pour la documentation de la version 2 ([doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr)) et pour l'espace d'échange de l'écosystème ([commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr) et [commun-demarche-numerique](/repos/demarche-numerique/commun-demarche-numerique)).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration majeure de l'OCR, de la précision d'extraction des RIB et ajout du traitement par lots.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Évolutions fonctionnelles sur la gestion des comptes et optimisations de l'infrastructure.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Diversification des modes de stockage et simplification des dépendances.
