# Synthèse d'activité : demarche-numerique (du 15/10 au 22/10)

## Résumé de l'activité
L'activité récente est marquée par une amélioration significative des capacités d'extraction de données avec [la_taupe](/repos/demarche-numerique/la_taupe) et un renforcement de la résilience du service principal [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), qui peut désormais fonctionner en mode dégradé en cas d'indisponibilité des API. 

Parallèlement, l'écosystème s'étend avec le lancement de nouveaux projets dédiés à la documentation de la version 2 et à la création d'espaces de collaboration communautaire ([doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr), [commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr) et [commun-demarche-numerique](/repos/demarche-numerique/commun-demarche-numerique)).

## Sécurité
- Renforcement de la sécurité des comptes "Super Admin" via l'ajout de l'OTP et du verrouillage de compte dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Sécurisation du serveur par l'implémentation d'un sandboxing pour le traitement des images dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Amélioration de la gestion des sessions et de la validation des jetons (JWT) et des URLs dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Extraction et OCR :** Intégration d'un nouveau moteur OCR plus performant et ajout de fonctionnalités de traitement par lots (batch) via la ligne de commande dans [la_taupe](/repos/demarche-numerique/la_taupe).
- **Stockage et Proxy :** Extension de la compatibilité avec les protocoles S3 et Swift dans [ds_proxy](/repos/demarche-numerique/ds_proxy).
- **Résilience et Infrastructure :** Introduction d'un mode de saisie dégradé pour les données SIRET/RNA et migration vers Sidekiq 8 dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Lancement de projets :** Initialisation des nouveaux dépôts de documentation et de partage pour l'écosystème ([doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr), [commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr) et [commun-demarche-numerique](/repos/demarche-numerique/commun-demarche-numerique)).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Évolutions majeures de l'OCR et ajout du traitement par lots.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Améliorations de la sécurité, de la résilience et des outils d'instruction.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Extension des capacités de stockage et optimisation technique.
